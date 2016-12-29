package Java.Trees;

import Java.Node;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by arnav on 12/25/2016.
 */
public class ReverseLevelOrderTraversal {

    public void reverseLevelOrderTraversal(Node root) {

        Stack<Node> stack = new Stack<>();
        Queue<Node> queue = new LinkedList<>();

        queue.offer(root);

        while(!queue.isEmpty()) {

            Node currentNode = queue.poll();

            stack.push(currentNode);

            if (currentNode.right != null) {

                queue.offer(currentNode.right);
            }

            if (currentNode.left != null) {

                queue.offer(currentNode.left);
            }
        }


        while(!stack.isEmpty()) {

            System.out.println(stack.pop().data);
        }

    }

    public void run() {

        Node root = new Node(10);

        root.left = new Node(20);
        root.right = new Node(30);

        root.left.left = new Node(40);
        root.left.right = new Node(50);

        root.right.right = new Node(60);

        reverseLevelOrderTraversal(root);

    }
}
