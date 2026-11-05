# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res=[]       
        def dfs(node, maxsofar):
            if not node:
                return

            if node.val >= maxsofar:
                res.append(node.val)
            
            maxsofar=max(node.val,maxsofar)

            dfs(node.left, maxsofar)
            dfs(node.right, maxsofar)
        dfs(root,root.val)
        return len(res)

        