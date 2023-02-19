# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]

        if not root:
            return ans

        q.append(root)

        while q:
            size=len(q)
            sub=[]
            for i in range(size):
                a=q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
                sub.append(a.val)
            ans.append(sub)

        ans= [ x  if i%2==0 else reversed(x) for i,x in enumerate(ans) ]
        return ans







