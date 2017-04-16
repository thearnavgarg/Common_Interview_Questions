package Java.Trees;

import Java.TreeNode;

/**
 * @author: Arnav Garg
 */
public class SizeOfBinaryTree {

    public int sizeOfBinaryTree(TreeNode root) {

        if (root == null) {
            return 0;
        }

        return 1 + sizeOfBinaryTree(root.left) + sizeOfBinaryTree(root.right);
    }

    public void run() {


        TreeNode root1 = new TreeNode(10);

        root1.left = new TreeNode(5);
        root1.right = new TreeNode(13);

        root1.left.left = new TreeNode(4);

        root1.right.left = new TreeNode(11);
        root1.right.right = new TreeNode(15);

        int size = sizeOfBinaryTree(root1);

        System.out.println(size);
    }
}
