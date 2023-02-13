class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        
        for src, dst in blueEdges:
            blue[src].append(dst)

        answer=[-1]*n

        q=deque()
        q.append([0, 0 , None]) #node, cost, prev edge color

        visited=set()
        visited.add((0,None))
        while q:
            node, cost, edge=q.popleft()
            if answer[node]==-1:
                answer[node]=cost
                
            if edge != "red":
                for adj in red[node]:
                    if (adj, "red") not in visited:
                        q.append([adj, cost+1, "red"])
                        visited.add((adj, "red"))
                
            if edge != "blue":
                for adj in blue[node]:
                    if (adj, "blue") not in visited:
                        q.append([adj, cost+1, "blue"])
                        visited.add((adj, "blue"))
        return answer

