# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        # Helper function
        #########################
        
        def inorder_traversal(root, sol_list, current_list):
            if not root:
                return
            current_list.append(root.val)
            if not root.left and not root.right:
                sol_list.append('->'.join([str(value) for value in current_list]))
                current_list.pop()
                return
            inorder_traversal(root.left, sol_list, current_list)
            inorder_traversal(root.right, sol_list, current_list)
            current_list.pop()
        #########################
        
        # base case
        if not root:
            return []
        
        current_list = []
        sol_list = []
        inorder_traversal(root, sol_list, current_list)
        return sol_list
