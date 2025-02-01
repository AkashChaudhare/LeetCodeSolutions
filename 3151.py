class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        curr_even = nums[0]%2 #0 if even, 1 if odd

        for num in nums[1:]:
            if num%2 != curr_even: #if both diff then continue, else break
                curr_even ^=1
            else:
                return False
            
        return True
