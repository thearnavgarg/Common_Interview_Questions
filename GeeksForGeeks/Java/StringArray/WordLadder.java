package Java.StringArray;

import java.util.ArrayList;

/**
 * Created by arnav on 12/8/16.
 */

//Given two words (start and end), and a dictionary, find the length of shortest transformation
// sequence from start to end, such that only one letter can be changed at a time and each intermediate word must exist
// in the dictionary. For example, given:
//
//        start = "hit"
//        end = "cog"
//        dict = ["hot","dot","dog","lot","log"]
//        One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program should return its length 5.


public class WordLadder {

    public boolean wordDiff(String s1, String s2) {

        int counter = 0;

        for (int i = 0; i < s1.length(); i++) {

            if(!( s1.charAt(i) == s2.charAt(i) ) ) {
                counter++;

                if (counter > 1) {
                    return false;
                }
            }
        }

        return true;
    }

    public int wordLadder(String start, String end, String[] dic) {

        ArrayList<String> list = new ArrayList<>();
        int counter  = 1;

        if(wordDiff(start, end)) {

            return 2;
        }

        while(!start.equals(end)) {

            if(wordDiff(start, end)) {

                counter++;
                start = end;
            }

            int flag = 0;

            for (int i = 0; i < dic.length; i++) {

                if(wordDiff(start, dic[i]) && !list.contains(dic[i])) {
                    flag = 1;
                    start = dic[i];
                    list.add(dic[i]);
                    counter++;
                    break;
                }
            }

            if(flag == 0) {
                return 0;
            }
        }

        return counter;
    }
}
