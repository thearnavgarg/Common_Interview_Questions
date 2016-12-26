package Trees;

public class Main {

    public static void main(String[] args) {

        HeightOfATree heightOfATree = new HeightOfATree();
        IsBinaryTree isBinaryTree = new IsBinaryTree();
        CheckBinaryTreesAreSame checkBinaryTreeSame = new CheckBinaryTreesAreSame();
        SizeOfBinaryTree sizeOfBinaryTree = new SizeOfBinaryTree();
        RootToLeafSum rootToLeafSum = new RootToLeafSum();
        ReverseLevelOrderTraversal reverseLevelOrderTraversal = new ReverseLevelOrderTraversal();
        LevelOrderTraversalSpiralOrder levelOrderTraversalSpiralOrder = new LevelOrderTraversalSpiralOrder();

        levelOrderTraversalSpiralOrder.run();
    }
}