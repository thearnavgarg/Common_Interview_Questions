package Java.Trees;

import Java.Node;

import java.util.Stack;

/**
 * Created by arnav on 12/26/2016.
 */
public class PostOrderWithOneStack {

    public void postOrderOneStack(Node root) {

        Stack<Node> stack = new Stack<>();
        Node current;

        stack.push(root);
        current = root.left;

        while (!stack.isEmpty() || current != null) {


            if(current != null) {

                stack.push(current);
                current = current.left;
            } else {

                Node node = stack.pop();
                System.out.println(node.data);

                if(stack.peek().right != node) {

                    current = stack.peek().right;
                } else {

                    System.out.println(stack.pop().data);
                }

            }
        }
    }

    public void run() {

        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);

        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        root.left.left.left = new Node(8);

        postOrderOneStack(root);
    }
}
