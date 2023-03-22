class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(dict)
        for s,d,cost in roads:
            graph[s][d]=cost
            graph[d][s]=cost
        q=deque()
        s=set()
        ans=float('inf')
        q.append(1)

        while q:
            node=q.popleft()
            if node in s:
                continue
            s.add(node)
            for neighbor in graph[node].keys():
                q.append(neighbor)
                ans=min(ans,graph[node][neighbor])
        return ans

