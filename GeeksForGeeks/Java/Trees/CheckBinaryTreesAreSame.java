package Java.Trees;

import Java.TreeNode;

/**
 * @author: Arnav Garg
 */
public class CheckBinaryTreesAreSame {


    /**
     *
     * This function first checks if both the roots reach the null at the same time. If they do, it returns a true.
     * After that check, if either of them is a null, then the next 'if-loop' will return a false;
     *
     * After we have verified that none of the nodes that we are checking are null, then we check if the values of the
     * nodes are different. If not, we more further down the tree.
     *
     * @param root1 : root of the first tree
     * @param root2 : root of the second tree
     * @return boolean value which is the answer.
     */
    public boolean checkBinaryTreeSame(TreeNode root1, TreeNode root2) {

        if(root1 == null && root2 == null) {
            return true;
        }

        if(root1 == null || root2 == null) {
            return false;
        }

        if(root1.data != root2.data) {
            return false;
        }

        return checkBinaryTreeSame(root1.left, root2.left) && checkBinaryTreeSame(root1.right, root2.right);
    }

    public void run() {

        TreeNode root1 = new TreeNode(10);

        root1.left = new TreeNode(5);
        root1.right = new TreeNode(13);

        root1.left.left = new TreeNode(4);

        root1.right.left = new TreeNode(11);
        root1.right.right = new TreeNode(15);


        TreeNode root2 = new TreeNode(10);

        root2.left = new TreeNode(5);
        root2.right = new TreeNode(13);

        root2.left.left = new TreeNode(4);

        root2.right.left = new TreeNode(11);
        root2.right.right = new TreeNode(1);


        System.out.println(checkBinaryTreeSame(root1, root2));

    }
}
