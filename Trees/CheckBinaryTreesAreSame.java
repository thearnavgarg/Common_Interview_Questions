package Trees;

/**
 * Created by arnav on 12/25/2016.
 */
public class CheckBinaryTreesAreSame {


    /**
     *
     * This function first checks if both the roots reach the null at the same time. If they do, it returns a true.
     * After that check, if either of them is a null, then the next 'if-loop' will return a false;
     *
     * After we have verified that none of the nodes that we are checking are null, then we check if the values of the
     * nodes are different. If not, we more further down the tree.
     *
     * @param root1 : root of the first tree
     * @param root2 : root of the second tree
     * @return boolean value which is the answer.
     */
    public boolean checkBinaryTreeSame(Node root1, Node root2) {

        if(root1 == null && root2 == null) {
            return true;
        }

        if(root1 == null || root2 == null) {
            return false;
        }

        if(root1.data != root2.data) {
            return false;
        }

        return checkBinaryTreeSame(root1.left, root2.left) && checkBinaryTreeSame(root1.right, root2.right);
    }

    public void run() {

        Node root1 = new Node(10);

        root1.left = new Node(5);
        root1.right = new Node(13);

        root1.left.left = new Node(4);

        root1.right.left = new Node(11);
        root1.right.right = new Node(15);


        Node root2 = new Node(10);

        root2.left = new Node(5);
        root2.right = new Node(13);

        root2.left.left = new Node(4);

        root2.right.left = new Node(11);
        root2.right.right = new Node(1);


        System.out.println(checkBinaryTreeSame(root1, root2));

    }
}
