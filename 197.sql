select l.id
from weather l inner join weather r
on datediff(l.recordDate, r.recordDate) = 1
and l.temperature > r.temperature
