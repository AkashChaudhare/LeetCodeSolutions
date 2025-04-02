select 
    round(avg(immediate)*100, 2) as immediate_percentage 
from
    (
        select 

        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rn,
        order_date = customer_pref_delivery_date as immediate,
        delivery_id

    from
        delivery
        ) t1 where rn = 1
