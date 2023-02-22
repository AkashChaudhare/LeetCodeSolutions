class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            need=1
            cap=0
            for w in weights:
                cap+=w
                if cap>capacity:
                    cap=w
                    need+=1
                    if need>days:
                        return False
            else:
                return True

        l=max(weights)
        r=sum(weights)

        while l<r:
            mid=l + (r-l)//2
            if possible(mid):
                r=mid
            else:
                l=mid+1
        return l
