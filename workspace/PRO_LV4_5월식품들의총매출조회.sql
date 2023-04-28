SELECT fp.product_id, product_name, (price * sum(amount)) as total_sales
from food_product fp
inner join food_order fo
    on fp.product_id = fo.product_id
where produce_date like '2022-05-%'
group by fo.product_id
having total_sales
order by total_sales desc, product_id asc