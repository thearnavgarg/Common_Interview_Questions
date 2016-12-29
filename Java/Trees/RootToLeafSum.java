package Java.Trees;

import Java.Node;

import java.util.ArrayList;

/**
 * Created by arnav on 12/25/2016.
 */
public class RootToLeafSum {


    public boolean root2LeafSum(Node root, int sum, ArrayList<Integer> result) {

        if (root == null) {
            return false;
        }

        if(root.left == null && root.right == null) {

            if (sum == root.data) {
                result.add(root.data);
                return true;
            } else {
                return false;
            }
        }

        sum -= root.data;

        if (root2LeafSum(root.left, sum, result) || root2LeafSum(root.right, sum, result)) {
            result.add(root.data);
            return true;
        } else {
            return false;
        }
    }

    public void run() {

        Node root = new Node(10);

        root.left = new Node(5);
        root.right = new Node(13);

        root.left.left = new Node(4);

        root.right.left = new Node(11);
        root.right.right = new Node(15);

        ArrayList<Integer> result = new ArrayList<>();
        boolean answer = root2LeafSum(root, 34, result);

        for (Integer value : result) {

            System.out.println(value + " ");
        }

        System.out.println(answer);


    }
}
