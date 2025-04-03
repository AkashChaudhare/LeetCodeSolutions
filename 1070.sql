select
    product_id,
    year as first_year,
    quantity, 
    price

from 
    (select
        product_id,
        year,
        quantity, 
        price,
        rank() over (partition by product_id order by year asc) as rn
    from sales) t1 
where t1.rn=1
order by product_id
