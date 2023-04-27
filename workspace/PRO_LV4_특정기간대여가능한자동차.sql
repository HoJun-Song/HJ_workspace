SELECT crcc.car_id,
       crcc.car_type,
       round(daily_fee * 0.3 * (100 - discount_rate)) as fee
from car_rental_company_car as crcc
    inner join car_rental_company_discount_plan as crcdp
        on crcc.car_type = crcdp.car_type and duration_type = '30일 이상'
where crcc.car_type in ('세단', 'SUV')
and crcc.car_id not in (
    select crcrh.car_id from car_rental_company_rental_history as crcrh
    where end_date >= '2022-11-01' and start_date <= '2022-11-30'
having 500000 <= fee and fee < 2000000
order by fee desc, crcc.car_type asc, crcc.car_id desc;