'''
Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
'''
def widthOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    from collections import namedtuple
    
    if not root:
        return 0
    
    Node = namedtuple('Node', ['address', 'position'])
    node = Node(root, 0)
    level = [node]
    ans = 0
    
    while level:
        ans = max(ans, level[-1].position - level[0].position + 1)
        new_level = []
        for node in level:
            if node.address.left:
                new_level.append(Node(node.address.left, node.position*2))
            if node.address.right:
                new_level.append(Node(node.address.right, (node.position*2)+1))
        level = new_level
    return ans