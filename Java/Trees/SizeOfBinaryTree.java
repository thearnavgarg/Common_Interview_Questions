package Java.Trees;

import Java.Node;

/**
 * Created by arnav on 12/25/2016.
 */
public class SizeOfBinaryTree {

    public int sizeOfBinaryTree(Node root) {

        if (root == null) {
            return 0;
        }

        return 1 + sizeOfBinaryTree(root.left) + sizeOfBinaryTree(root.right);
    }


    public void run() {


        Node root1 = new Node(10);

        root1.left = new Node(5);
        root1.right = new Node(13);

        root1.left.left = new Node(4);

        root1.right.left = new Node(11);
        root1.right.right = new Node(15);

        int size = sizeOfBinaryTree(root1);

        System.out.println(size);
    }
}
