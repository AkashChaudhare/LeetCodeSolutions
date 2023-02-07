class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types=dict()
        l=0
        r=0
        max_fruits=0

        while r<len(fruits):
            types[fruits[r]]=types.get(fruits[r], 0)+1

            while len(types)>2:
                types[fruits[l]]-=1
                if types[fruits[l]]==0:
                    types.pop(fruits[l])
                l+=1
            
            max_fruits=max(max_fruits,r-l+1)
            r+=1
        return max_fruits
