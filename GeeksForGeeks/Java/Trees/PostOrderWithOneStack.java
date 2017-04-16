package Java.Trees;

import Java.TreeNode;

import java.util.Stack;

/**
 * @author: Arnav Garg
 */
public class PostOrderWithOneStack {

    public void postOrderOneStack(TreeNode root) {

        Stack<TreeNode> stack = new Stack<>();
        TreeNode current;

        stack.push(root);
        current = root.left;

        while (!stack.isEmpty() || current != null) {


            if(current != null) {

                stack.push(current);
                current = current.left;
            } else {

                TreeNode treeNode = stack.pop();
                System.out.println(treeNode.data);

                if(stack.peek().right != treeNode) {

                    current = stack.peek().right;
                } else {

                    System.out.println(stack.pop().data);
                }

            }
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

        postOrderOneStack(root);
    }
}
