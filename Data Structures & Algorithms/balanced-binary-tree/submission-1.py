# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balancedtree=True

        def height(root):
            nonlocal balancedtree
            if not root:
                return 0
            
            a=height(root.left)
            b=height(root.right)

            if abs(a-b)>1:
                balancedtree=False
                return 0
            return 1 + max(height(root.left), height(root.right))
        height(root)
        return balancedtree