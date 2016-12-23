package StringArray;

import java.util.HashMap;

/**
 * Created by arnav on 12/8/16.
 */

/*
    Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

        For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.
*/

/*
*  egg and add are isomorphic
*  aadc and eefd be isomorphic? => NO
*
*  hashmap
*  e -> a
*  g -> d
*
*
*  timecomplexity: O(n)
* */

public class IsomorphicStrings {

    public boolean isoStrings(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Character> map = new HashMap<>();
        StringBuffer sb = new StringBuffer();
        Character atCurrentPos;

        for(int i = 0; i < s.length(); i++) {

            if (map.containsKey(s.charAt(i))) {

                atCurrentPos = map.get(s.charAt(i));

                if(atCurrentPos != t.charAt(i)) {
                    return false;
                }

            } else {

                map.put(s.charAt(i), t.charAt(i));
                atCurrentPos = t.charAt(i);
            }
        }

        return true;
    }
}




































