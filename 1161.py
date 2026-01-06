# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def recurse(node, ddd, level):
            if node:
                ddd[level] = ddd.get(level, 0) + node.val
                recurse(node.left, ddd, level + 1)
                recurse(node.right, ddd, level + 1)

        ddd = {}
        recurse(root, ddd, 1)

        # ddd = [[v,k] for k,v in ddd.items()]

        max_sum = float("-inf")
        min_lvl = float("inf")

        for level, lvl_sum in ddd.items():
            if lvl_sum > max_sum:
                min_lvl, max_sum = level, lvl_sum
            elif lvl_sum == max_sum and level<min_lvl:
                min_lvl = level

        return min_lvl


                
            
