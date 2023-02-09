class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        
        nums=[(num, i) for i, num in enumerate(nums)]
        nums.sort()

        l=0
        r=len(nums)-1

        while(l<=r):
            if nums[l][0]+nums[r][0]==target:
                return [nums[l][1] , nums[r][1]]
            elif nums[l][0]+nums[r][0]<target:
                l+=1
            else:
                r-=1
        return 0
      
      
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        ddd=dict()

        for i, num in enumerate(nums):
            if num in ddd:
                return [i , ddd[num]]
            else:
                ddd[target-num]=i
        return 0
