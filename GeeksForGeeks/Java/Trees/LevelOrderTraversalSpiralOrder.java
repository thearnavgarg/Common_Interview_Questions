package Java.Trees;

import Java.TreeNode;

import java.util.Stack;

/**
 * Created by arnav on 12/25/2016.
 */
public class LevelOrderTraversalSpiralOrder {


    public void levelOrderTraversalSpiralOrder(TreeNode root) {

        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();

        stack1.add(root);

        while(!stack1.isEmpty() || !stack2.isEmpty()) {

            while(!stack1.isEmpty()) {

                TreeNode currentTreeNode = stack1.pop();
                System.out.println(currentTreeNode.data);

                if (currentTreeNode.left != null) {
                    stack2.push(currentTreeNode.left);
                }

                if (currentTreeNode.right != null) {
                    stack2.push(currentTreeNode.right);
                }

            }

            while(!stack2.isEmpty()) {

                TreeNode currentTreeNode = stack2.pop();
                System.out.println(currentTreeNode.data);

                if (currentTreeNode.right != null) {
                    stack1.push(currentTreeNode.right);
                }

                if (currentTreeNode.left != null) {
                    stack1.push(currentTreeNode.left);
                }
            }
        }
    }


    public void run() {

        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(20);
        root.right = new TreeNode(30);

        root.left.left = new TreeNode(40);
        root.left.right = new TreeNode(50);

        root.right.right = new TreeNode(60);

        levelOrderTraversalSpiralOrder(root);
    }
}
