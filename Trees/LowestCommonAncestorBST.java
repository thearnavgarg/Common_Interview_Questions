package Trees;

/**
 * Created by arnav on 12/26/2016.
 */
public class LowestCommonAncestorBST {


    public Node lowestCommonAncestorBST(Node root, int data1, int data2) {

        if(root == null) {
            return null;
        }

        if((root.data > data1 && root.data < data2)
                || root.data < data1 && root.data > data2 ) {

            return root;
        }

        if (root.data > data1 && root.data > data2) {
            return lowestCommonAncestorBST(root.left, data1, data2);

        } else{
            return lowestCommonAncestorBST(root.right, data1, data2);
        }
    }


    public void run() {

        Node root = new Node(10);

        root.left = new Node(5);
        root.right = new Node(13);

        root.left.left = new Node(4);

        root.right.left = new Node(11);
        root.right.right = new Node(15);

        Node answer = lowestCommonAncestorBST(root, 15,11);

        if(answer != null) {

            System.out.println(answer.data);
        } else {
        }
    }
}
