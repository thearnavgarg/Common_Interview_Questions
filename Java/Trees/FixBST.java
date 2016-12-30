package Java.Trees;

import Java.TreeNode;

import java.util.ArrayList;

/**
 * Created by arnav on 12/29/16.
 */
public class FixBST {

    /**
     * This is basically for checking if the code is working. You can ignore this and skip to the run function.
     * @param root
     */
    public void inorder(TreeNode root) {

        if (root == null) {

            return;
        }

        inorder(root.left);
        System.out.println(root.data);
        inorder(root.right);
    }

    /**
     * traversing in-order and storing all the values of the data in data storage and nodes in nodestorage.
     * @param root : root of the tree
     * @param dataStorage : arraylist for storing all the data of the nodes
     * @param nodeStorage : arraylist for storing all the nodes.
     */
    public void modifiedInorder(TreeNode root, ArrayList<Integer> dataStorage, ArrayList<TreeNode> nodeStorage) {

        //base condition
        if (root == null) {
            return;
        }

        //going left
        modifiedInorder(root.left, dataStorage, nodeStorage);

        //storing all the values
        dataStorage.add(root.data);
        nodeStorage.add(root);

        //going right
        modifiedInorder(root.right, dataStorage, nodeStorage);
    }

    public void run() {

        TreeNode root = new TreeNode(10);

        root.left = new TreeNode(15);
        root.right = new TreeNode(13);

        root.left.left = new TreeNode(4);

        root.right.left = new TreeNode(11);
        root.right.right = new TreeNode(5);



        ArrayList<Integer> dataStorage = new ArrayList<>();
        ArrayList<TreeNode> nodeStorage = new ArrayList<>();

        //calling the modifiedInorder traversal for getting the dataStorage and nodeStorage values
        modifiedInorder(root, dataStorage, nodeStorage);

        //the two numbers that need to be swapped.
        int[] swappedInts = new int[2];

        //storing default values to check if the values have been filled or not.
        swappedInts[0] = Integer.MIN_VALUE;
        swappedInts[1] = Integer.MAX_VALUE;

        for (int i = 0; i < dataStorage.size()-1; i++) {

            //checking for the faults in the in-order check. If the increasing order is not followed, then we will
            //fill the swap array.
            if ( dataStorage.get(i) > dataStorage.get(i+1) ) {

                if (swappedInts[0] == Integer.MIN_VALUE) {

                    swappedInts[0] = i;
                    swappedInts[1] = i + 1;
                } else {

                    swappedInts[1] = i+1;
                    break;
                }
            }
        }

        int tempData = nodeStorage.get(swappedInts[0]).data;
        nodeStorage.get(swappedInts[0]).data = nodeStorage.get(swappedInts[1]).data;
        nodeStorage.get(swappedInts[1]).data = tempData;

        inorder(root);
    }
}
