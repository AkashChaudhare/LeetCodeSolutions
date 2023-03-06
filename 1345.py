import collections
class Solution:
    def minJumps(self, arr):
        
        visited=[-1]*len(arr)
        steps=[-1]*len(arr)
        ddd=collections.defaultdict(list)

        for i, val in enumerate(arr):
            ddd[val].append(i)
        #print(ddd)
        q=collections.deque()
        q.append((0,0))

        while q:
            #print(q)
            #print(visited)
            idx, cost=q.popleft()
            visited[idx]=cost
            if idx==len(arr)-1:
                print(cost)
                return cost
            #print(ddd[arr[idx]])
            if ddd[arr[idx]]!=None:
                for n in ddd[arr[idx]]:
                    #print(n)
                    #if n==len(arr)-1:
                        #print('direct return was exced')
                    #    print(cost+1)
                    #    return cost+1
                    if visited[n]==-1:
                        visited[n]=cost+1
                        q.append((n,cost+1))
                    ddd[arr[idx]]=None
            if idx>0 and visited[idx-1]==-1:
                    q.append((idx-1,cost+1))
            if idx<len(arr)-1 and visited[idx+1]==-1:
                    q.append((idx+1,cost+1))
        print(visited[len(arr)-1])
        return min(visited[len(arr)-1],len(arr))
        
        
        
        
#a=Solution()
#a.minJumps([100,-23,-23,404,100,23,23,23,3,404])
#a.minJumps([7])
#a.minJumps([7,6,9,6,9,6,9,7])
#a.minJumps([7,1])
#a.minJumps([7,7])
