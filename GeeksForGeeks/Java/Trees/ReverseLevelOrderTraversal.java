package Java.Trees;

import Java.TreeNode;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by arnav on 12/25/2016.
 */
public class ReverseLevelOrderTraversal {

    public void reverseLevelOrderTraversal(TreeNode root) {

        Stack<TreeNode> stack = new Stack<>();
        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);

        while(!queue.isEmpty()) {

            TreeNode currentTreeNode = queue.poll();

            stack.push(currentTreeNode);

            if (currentTreeNode.right != null) {

                queue.offer(currentTreeNode.right);
            }

            if (currentTreeNode.left != null) {

                queue.offer(currentTreeNode.left);
            }
        }


        while(!stack.isEmpty()) {

            System.out.println(stack.pop().data);
        }

    }

    public void run() {

        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(20);
        root.right = new TreeNode(30);

        root.left.left = new TreeNode(40);
        root.left.right = new TreeNode(50);

        root.right.right = new TreeNode(60);

        reverseLevelOrderTraversal(root);

    }
}
