# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: list[list[int]]) -> TreeNode | None:
        acha = {}
        root = set()
        for i in range(len(desc)):
            root.add(desc[i][0])
        for p,c,l in desc:
            if c in root:
                root.remove(c)
            if p not in acha:
                acha[p] = [-1 , -1]
            acha[p][l] = c
        print(acha)
        print(root)

        def dfs(node):
            if node not in acha:
                return TreeNode(node)
            newNode = TreeNode(node)
            if acha[node][0] != -1:
                newNode.right = dfs(acha[node][0])
            if acha[node][1] != -1:
                newNode.left = dfs(acha[node][1])
            return newNode
        return dfs(list(root)[0])
        
        






















