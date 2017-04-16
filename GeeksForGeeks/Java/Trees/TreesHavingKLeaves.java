package Java.Trees;

import Java.TreeNode;

/**
 * @author: Arnav Garg
 */
public class TreesHavingKLeaves {


    /**
     * Would do a post-order traversal and would return the number of nodes traversed so far and at any point it hits
     * the desired number, it would print.
     * @param root
     * @param k : the number leaves we want the
     * @return
     */
    public int treesHavingKLeaves(TreeNode root, int k) {

        //base check that the root value is not null
        if (root == null) {

            return 0;
        }

        // leaf node
        if (root.left == null && root.right == null) {
            return 1;
        }

        //Finding the leaf nodes in the left tree
        int leftLeaves = treesHavingKLeaves(root.left, k);

        //Finding the leaf nodes in the right tree
        int rightLeaves = treesHavingKLeaves(root.right, k);


        //checking if the nodes in the right and left tree are the same.
        if (leftLeaves + rightLeaves == k) {

            System.out.println(root.data);
        }

        //returning the sum of the left sub-tree leaves and right sub-tree leaves.
        return leftLeaves + rightLeaves;

    }


    public void run() {

        TreeNode root = new TreeNode(1);

        root.left = new TreeNode(2);
        root.right = new TreeNode(4);

        root.left.left = new TreeNode(5);
        root.left.right = new TreeNode(6);
        root.right.left = new TreeNode(7);
        root.right.right = new TreeNode(8);

        root.left.left.left = new TreeNode(9);
        root.left.left.right = new TreeNode(10);
        root.right.left.left = new TreeNode(11);
        root.right.left.right = new TreeNode(12);

        treesHavingKLeaves(root, 2);
    }
}
