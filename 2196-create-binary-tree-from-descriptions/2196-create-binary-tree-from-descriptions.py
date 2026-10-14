# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: list[list[int]]) -> Optional[TreeNode] | None:
        nodes = [None] * 100001
        root = None

        for _, v, _ in desc:
            nodes[v] = TreeNode(v)
        for u, v, left in desc:
            if nodes[u] is None:
                nodes[u] = TreeNode(u)
                root = nodes[u]
            if left == 1:
                nodes[u].left = nodes[v]
            else:
                nodes[u].right = nodes[v]
    
        return root


