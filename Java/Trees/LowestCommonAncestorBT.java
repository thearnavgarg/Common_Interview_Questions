package Java.Trees;

/**
 * Created by arnav on 12/26/2016.
 */
public class LowestCommonAncestorBT {


    public Node lowestCommonAncestorBT(Node root, int data1, int data2) {

        if(root == null) {
            return null;
        }

        if(root.data == data1 || root.data == data2) {
            return root;
        }

        Node nodeLeft = lowestCommonAncestorBT(root.left, data1, data2);
        Node nodeRight = lowestCommonAncestorBT(root.right, data1, data2);

        if( nodeLeft != null && nodeRight != null) {
            return root;
        } else if (nodeLeft != null) {
            return root.left;
        } else if (nodeRight != null) {
            return root.right;
        } else {
            return null;
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

        Node answer = lowestCommonAncestorBT(root, 8,7);

        if(answer != null) {
            System.out.println(answer.data);
        }
    }
}
