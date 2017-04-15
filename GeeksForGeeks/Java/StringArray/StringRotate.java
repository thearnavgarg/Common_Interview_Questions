package Java.StringArray;

/**
 * Created by arnav on 11/22/16.
 */

/*
* Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
* The input string does not contain leading or trailing spaces and the words are always separated by a single space.
* */
public class StringRotate {

    public void stringRotate(String s) {

        String[] stringArray = s.split(" ");

        int start = 0;
        int end = stringArray.length-1;

        //reversing the string
        while(start <= end) {
            String temp = stringArray[start];
            stringArray[start] = stringArray[end];
            stringArray[end] = temp;
            start++;
            end--;
        }

        for(int i = 0; i < stringArray.length; i++) {
            System.out.print(stringArray[i] + " ");
        }
    }
}
