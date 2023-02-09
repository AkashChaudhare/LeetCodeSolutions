class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache=defaultdict(int)
        for char in s:
            cache[char]+=1
        #print(cache)

        def check(d1,d2):
            for k1 in d1:
                if d1[k1]!=d2[k1]:
                    return False
            return True

        cache2=dict()
        ans=[]
        for char in s:
            cache2[char]=cache2.get(char,0)+1
            if check(cache2, cache):
                ans.append(s.rfind(char)+1)
                for k in cache2:
                    del cache[k]
                cache2=dict()


        for i in range(len(ans)-1,0,-1):
            ans[i]-=ans[i-1]



        return ans
