package Trees;

import java.util.ArrayList;

/**
 * Created by arnav on 12/22/16.
 */
public class TestCases {


    ArrayList<Node> btRootList;
    ArrayList<Node> treeRootList;

    public TestCases() {

        btRootList = new ArrayList<>();
        treeRootList = new ArrayList<>();

        createTestCases();
    }

    public void createBinarySearchTreeHelper(int data, Node root) {

        //System.out.println("Data : " + data);

        if (data <= root.data && root.left == null) {

            Node newNode = new Node(data, null, null);
            root.left = newNode;
            return;
        } else if(data > root.data && root.right == null) {
            Node newNode = new Node(data, null, null);
            root.right = newNode;
            return;

        }

        if (data <= root.data) {
            createBinarySearchTreeHelper(data, root.left);
        } else {
            createBinarySearchTreeHelper(data, root.right);
        }

    }

    public Node createBinarySearchTree(int[] data, Node root) {

        int counter = 1;

        if(root == null && data.length == 0) {
            return null;
        }

        if(root == null) {
            root = new Node(data[0], null, null);
        }


        for (int i = 1; i < data.length; i++) {

            createBinarySearchTreeHelper(data[i], root);
        }

        return root;
    }

    public void printTree (Node root) {

        if(root == null) {
             return;
        }

        printTree(root.left);
        System.out.println(root.data);
        printTree(root.right);
    }

    public void createTestCases() {

        //testcases for BST
        btRootList.add(createBinarySearchTree(new int[]{}, null));
        btRootList.add(createBinarySearchTree(new int[]{1,2,3,4,5,6,7,8}, null));
        btRootList.add(createBinarySearchTree(new int[]{1,1,2,2,3,3,4,4}, null));
        btRootList.add(createBinarySearchTree(new int[]{1,2,3,4,5,6,7,8}, null));
        btRootList.add(createBinarySearchTree(new int[]{1}, null));
        btRootList.add(createBinarySearchTree(new int[]{1,2,3,4,5,6,7,8}, null));


        treeRootList.add(null);

        //testcases for Normal Trees
        Node root = new Node(0, null, null);

        root.left = new Node(1,null, null);
        root.right = new Node(12, null, null);

        root.left.left = new Node(2,null, null);
        root.left.right = new Node(3, null, null);

        root.right.left = new Node(6,null, null);
        root.right.right = new Node(7,null, null);

        treeRootList.add(root);

    }

    public ArrayList<Node> getBtRootList() {
        return btRootList;
    }

    public ArrayList<Node> getTreeRootList() {
        return treeRootList;
    }

}
