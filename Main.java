import StringArray.IsomorphicStrings;
import StringArray.RotateArray;
import StringArray.StringRotate;
import StringArray.WordLadder;
import Trees.*;

/**
 * Created by arnav on 12/26/2016.
 */
public class Main {

    public static void main(String[] args) {

        //Trees.
        HeightOfATree heightOfATree = new HeightOfATree();
        IsBinaryTree isBinaryTree = new IsBinaryTree();
        CheckBinaryTreesAreSame checkBinaryTreeSame = new CheckBinaryTreesAreSame();
        SizeOfBinaryTree sizeOfBinaryTree = new SizeOfBinaryTree();
        RootToLeafSum rootToLeafSum = new RootToLeafSum();
        ReverseLevelOrderTraversal reverseLevelOrderTraversal = new ReverseLevelOrderTraversal();
        LevelOrderTraversalSpiralOrder levelOrderTraversalSpiralOrder = new LevelOrderTraversalSpiralOrder();
        LowestCommonAncestorBST lowestCommonAncestorBST = new LowestCommonAncestorBST();
        LowestCommonAncestorBT lowestCommonAncestorBT = new LowestCommonAncestorBT();
        PostOrderWithOneStack postOrderWithOneStack = new PostOrderWithOneStack();

        //Strings.
        RotateArray rotateArray = new RotateArray();
        StringRotate stringRotate = new StringRotate();
        IsomorphicStrings isomorphicStrings = new IsomorphicStrings();
        WordLadder wordLadder = new WordLadder();

        postOrderWithOneStack.run();

    }
}
