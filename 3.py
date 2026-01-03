class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        past = set()
        l=0
        
        res = 0

        for r, char in enumerate(s):
            print(past)
            if char in past:
                while char in past:
                    past.remove(s[l])
                    l+=1
            
            past.add(char)
            res = max(res, (r-l+1))

        return res
