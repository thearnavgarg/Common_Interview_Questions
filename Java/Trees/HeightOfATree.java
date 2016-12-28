package Java.Trees;

/**
 * Created by arnav on 12/25/2016.
 */
public class HeightOfATree {


    public int heightOfTree(Node root) {

        if(root == null) {
            return 0;
        }

        return 1 + Math.max(heightOfTree(root.left), heightOfTree(root.right));
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


        System.out.println(heightOfTree(root));

    }
}
