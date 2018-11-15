'''Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.'''

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    class NodeInfo:
        __slots__ = ['found', 'parent']
        
        def __init__(self, found, parent):
            self.found = found
            self.parent = parent
    
    
    def lca_helper(root, p, q):
        if not root:
            return NodeInfo(False, root)
        
        if root == p or root == q:
            parent = p if root == p else q
            return NodeInfo(True, parent)
        
        leftInfo = lca_helper(root.left, p, q)
        rightInfo = lca_helper(root.right, p, q)


        
        if rightInfo.found and leftInfo.found:
            return NodeInfo(True, root)
        
        if rightInfo.found or leftInfo.found:
            parent = rightInfo.parent if rightInfo.found else leftInfo.parent
            return NodeInfo(True, parent)
        
        return NodeInfo(False, None)
        
    if not root:
        return None
    
    lca = lca_helper(root, p, q)
    return lca.parent
