SELECT user_id,COUNT(follower_id) as followers_count
from Followers
GROUP BY user_id
ORDER BY user_id;
