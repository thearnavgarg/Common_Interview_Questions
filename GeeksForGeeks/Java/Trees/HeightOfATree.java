package Java.Trees;

import Java.TreeNode;

/**
 * Created by arnav on 12/25/2016.
 */
public class HeightOfATree {


    public int heightOfTree(TreeNode root) {

        if(root == null) {
            return 0;
        }

        return 1 + Math.max(heightOfTree(root.left), heightOfTree(root.right));
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


        System.out.println(heightOfTree(root));

    }
}
