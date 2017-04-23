package Java.Trees;

import Java.TreeNode;

/**
 * @author: Arnav Garg
 */
public class LowestCommonAncestorBT {


    public TreeNode lowestCommonAncestorBT(TreeNode root, int data1, int data2) {

        if(root == null) {
            return null;
        }

        if(root.data == data1 || root.data == data2) {
            return root;
        }

        TreeNode treeNodeLeft = lowestCommonAncestorBT(root.left, data1, data2);
        TreeNode treeNodeRight = lowestCommonAncestorBT(root.right, data1, data2);

        if( treeNodeLeft != null && treeNodeRight != null) {
            return root;
        } else if (treeNodeLeft != null) {
            return root.left;
        } else if (treeNodeRight != null) {
            return root.right;
        } else {
            return null;
        }
    }

    public void run() {


        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        root.left.left.left = new TreeNode(8);

        TreeNode answer = lowestCommonAncestorBT(root, 8,7);

        if(answer != null) {
            System.out.println(answer.data);
        }
    }
}
