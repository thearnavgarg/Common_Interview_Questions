package Trees;

/**
 * Created by arnav on 12/25/2016.
 */
public class IsBinaryTree {


    public boolean isBinary(Node root, int min, int max) {

        if (root == null) {
            return true;
        }

        if (root.data < min || root.data > max) {
            return false;
        }

        return isBinary(root.left, min, root.data) && isBinary(root.right, root.data, max);

    }

    public void run() {
        /*
        *
        *            10
        *       5           13
        *    4          11      15
        * */

        Node root = new Node(10);

        root.left = new Node(5);
        root.right = new Node(13);

        root.left.left = new Node(4);

        root.right.left = new Node(11);
        root.right.right = new Node(1);

        System.out.println(isBinary(root, Integer.MIN_VALUE, Integer.MAX_VALUE));
    }
}
