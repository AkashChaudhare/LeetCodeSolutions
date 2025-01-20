select
  l.machine_id, round(avg(r.timestamp)-avg(l.timestamp), 3) as processing_time
from 
    (select * from activity where activity_type = 'start') l
    inner join (select * from activity where activity_type = 'end') r
    
on l.machine_id = r.machine_id 
    and l.process_id = r.process_id
  
group by machine_id
