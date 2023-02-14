class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        n=len(roads)+1
        visited=[0]*n
        visited[0]=1
        
        graph=defaultdict(list)

        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        Fuel=0

        def dfs( node):
            nonlocal Fuel
            people=0
            for adj in graph[node]:
                if  visited[adj]==0:
                    #print(node,'to', adj)
                    visited[adj]=1
                    p=dfs(adj)
                    people+=p
                    Fuel+=int(ceil(p/seats))
            return people+1
        dfs(0)
        return Fuel

            
