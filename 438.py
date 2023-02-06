class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def makelist(a):
            lll=[0]*26
            for c in a:
                lll[ord(c)-97]+=1
            return lll

        pattern=makelist(p)
        string=makelist(s[:len(p)])

        print(pattern)
        print(string)
        ans=[]
        if pattern==string:
            ans.append(0)

        l , r = 0 , len(p)

        while(r<len(s)):
            string[ord(s[r])-97]+=1
            string[ord(s[l])-97]-=1
            print(string)
            if pattern==string:
                print(l)
                ans.append(l+1)
            r+=1
            l+=1
            
        return ans
