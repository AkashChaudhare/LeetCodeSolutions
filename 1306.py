class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=[start]
        s={start}

        while q:
            #print(q)
            node=q.pop(0)
            if arr[node]==0:
                return True
            if node-arr[node] >= 0:
                if node-arr[node] not in s:
                    q.append(node-arr[node])
                    s.add(node-arr[node])

            if node+arr[node] < len(arr):
                if node+arr[node] not in s:
                    q.append(node+arr[node])
                    s.add(node+arr[node])
        return False
