package StringArray;

/**
 * Created by arnav on 11/22/16.
 */
public class Main {

    public static void main(String[] args) {

        RotateArray rotateArray = new RotateArray();
        StringRotate stringRotate = new StringRotate();
        IsomorphicStrings isomorphicStrings = new IsomorphicStrings();
        WordLadder wordLadder = new WordLadder();

//        System.out.println(wordLadder.wordLadder("hit", "cog", new String[] {"hot","dot","dog","lot","log"}));

        System.out.println(isomorphicStrings.isoStrings("foo", "bar"));
//        stringRotate.stringRotate("the sky is blue");

        System.out.println("--over--");
    }
}
