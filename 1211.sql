select
    query_name,
    round(avg(quality_sum_total),2) as quality,
    round(avg(is_low_rating)*100,2) as poor_query_percentage 
from
    (select
        query_name,
        rating/position as quality_sum_total,
        case when rating<3 then 1 else 0 end as is_low_rating
    from
        queries) t1

group by t1.query_name
