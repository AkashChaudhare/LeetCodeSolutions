class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        min_req_to_be_highest = max(candies) - extraCandies

        res = []
        for can in candies:
            if can < min_req_to_be_highest:
                res.append(False)
            else:
                res.append(True)
        return res
