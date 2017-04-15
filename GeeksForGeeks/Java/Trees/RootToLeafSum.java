package Java.Trees;

import Java.TreeNode;

import java.util.ArrayList;

/**
 * Created by arnav on 12/25/2016.
 */
public class RootToLeafSum {


    public boolean root2LeafSum(TreeNode root, int sum, ArrayList<Integer> result) {

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

        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(5);
        root.right = new TreeNode(13);

        root.left.left = new TreeNode(4);

        root.right.left = new TreeNode(11);
        root.right.right = new TreeNode(15);

        ArrayList<Integer> result = new ArrayList<>();
        boolean answer = root2LeafSum(root, 34, result);

        for (Integer value : result) {

            System.out.println(value + " ");
        }

        System.out.println(answer);


    }
}
