package Java.Trees;

import Java.TreeNode;

/**
 * @author: Arnav Garg
 */
public class LargestBSTSubtree {

    private class TreeNodeWrapper{

        public boolean isBST;
        int max;
        int min;
        int size;

        TreeNodeWrapper(boolean isBST, int max, int min, int size) {

            this.isBST = isBST;
            this.max = max;
            this.min = min;
            this.size = size;
        }
    }


    public TreeNodeWrapper largestBSTSubtree(TreeNode root) {

        if (root == null) {

            return new TreeNodeWrapper(true, Integer.MIN_VALUE, Integer.MAX_VALUE, 0);
        }

        TreeNodeWrapper leftTreeNode = largestBSTSubtree(root.left);
        TreeNodeWrapper rightTreeNode = largestBSTSubtree(root.right);


        if (leftTreeNode.isBST == true && rightTreeNode.isBST == true &&
                root.data > leftTreeNode.max && root.data < rightTreeNode.min) {

            int min = (leftTreeNode.min == Integer.MAX_VALUE) ? root.data : leftTreeNode.min;
            int max = (rightTreeNode.max == Integer.MIN_VALUE) ? root.data : rightTreeNode.max;
            int size = rightTreeNode.size + leftTreeNode.size + 1;

            return new TreeNodeWrapper(true, max, min, size);

        } else if (leftTreeNode.isBST == true || rightTreeNode.isBST == true) {


            int max = 0;
            int min = 0;
            int size = Math.max(rightTreeNode.size, leftTreeNode.size);

            return new TreeNodeWrapper(false, max, min, size);

        } else {

            return new TreeNodeWrapper(false, 0, 0, 1);
        }
    }

    public void run() {


        TreeNode root = new TreeNode(50);

        root.left = new TreeNode(10);
        root.right = new TreeNode(60);

        root.left.left = new TreeNode(5);
        root.left.right = new TreeNode(20);

        root.right.left = new TreeNode(55);
        root.right.right = new TreeNode(70);

        root.right.left.left = new TreeNode(52);

        root.right.right.left = new TreeNode(65);
        root.right.right.right = new TreeNode(80);

        TreeNodeWrapper treeNodeWrapper = largestBSTSubtree(root);

        if(treeNodeWrapper == null) {

            System.out.println("No Tree available");
            return;
        }

        System.out.println(treeNodeWrapper.size);
    }
}
