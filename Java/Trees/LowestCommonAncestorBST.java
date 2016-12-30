package Java.Trees;

import Java.TreeNode;

/**
 * Created by arnav on 12/26/2016.
 */
public class LowestCommonAncestorBST {

    public TreeNode lowestCommonAncestorBST(TreeNode root, int data1, int data2) {

        if(root == null) {
            return null;
        }

        if((root.data > data1 && root.data < data2)
                || root.data < data1 && root.data > data2 ) {

            return root;
        }

        if (root.data > data1 && root.data > data2) {
            return lowestCommonAncestorBST(root.left, data1, data2);

        } else{
            return lowestCommonAncestorBST(root.right, data1, data2);
        }
    }


    public void run() {

        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(5);
        root.right = new TreeNode(13);

        root.left.left = new TreeNode(4);

        root.right.left = new TreeNode(11);
        root.right.right = new TreeNode(15);

        TreeNode answer = lowestCommonAncestorBST(root, 15,11);

        if(answer != null) {

            System.out.println(answer.data);
        } else {
        }
    }
}
