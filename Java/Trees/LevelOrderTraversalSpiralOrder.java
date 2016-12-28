package Java.Trees;

import java.util.Stack;

/**
 * Created by arnav on 12/25/2016.
 */
public class LevelOrderTraversalSpiralOrder {

    public void levelOrderTraversalSpiralOrder(Node root) {

        Stack<Node> stack1 = new Stack<>();
        Stack<Node> stack2 = new Stack<>();

        stack1.add(root);

        while(!stack1.isEmpty() || !stack2.isEmpty()) {

            while(!stack1.isEmpty()) {

                Node currentNode = stack1.pop();
                System.out.println(currentNode.data);

                if (currentNode.left != null) {
                    stack2.push(currentNode.left);
                }

                if (currentNode.right != null) {
                    stack2.push(currentNode.right);
                }

            }

            while(!stack2.isEmpty()) {

                Node currentNode = stack2.pop();
                System.out.println(currentNode.data);

                if (currentNode.right != null) {
                    stack1.push(currentNode.right);
                }

                if (currentNode.left != null) {
                    stack1.push(currentNode.left);
                }
            }
        }
    }


    public void run() {

        Node root = new Node(10);

        root.left = new Node(20);
        root.right = new Node(30);

        root.left.left = new Node(40);
        root.left.right = new Node(50);

        root.right.right = new Node(60);

        levelOrderTraversalSpiralOrder(root);
    }
}
