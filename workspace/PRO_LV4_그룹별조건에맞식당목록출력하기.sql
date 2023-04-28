with etc as (
    select member_id, rank() over(order by count(*) desc) as re
    from rest_review
    group by member_id
)
select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from member_profile
    inner join rest_review on member_profile.member_id = rest_review.member_id
where member_profile.member_id in (
    select etc.member_id
    from etc
    where re = 1
)
order by review_date, review_text