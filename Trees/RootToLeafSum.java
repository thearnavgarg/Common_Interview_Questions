package Trees;

/**
 * Created by arnav on 12/25/2016.
 */
public class RootToLeafSum {


    public boolean root2LeafSum(Node root, int sum) {

        if (root == null) {
            return false;
        }

        if(root.left == null && root.right == null) {

            if (sum == root.data) {
                return true;
            } else {
                return false;
            }
        }

        sum -= root.data;

        return root2LeafSum(root.left, sum) || root2LeafSum(root.right, sum);
    }

    public void run() {

        Node root = new Node(10);

        root.left = new Node(5);
        root.right = new Node(13);

        root.left.left = new Node(4);

        root.right.left = new Node(11);
        root.right.right = new Node(15);

        boolean answer = root2LeafSum(root, 34);

        System.out.println(answer);


    }
}
