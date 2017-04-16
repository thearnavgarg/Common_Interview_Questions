package Java.StringArray;

/**
 * @author: Arnav Garg
 */
public class PermutationPalindrome {

    public boolean PermutationPalindrome(String string) {

        if (string.length() == 0) {
            return true;
        }

        int[] map = new int[128];
        char[] char_array = string.toCharArray();

        for (char ch : char_array) {

            if (ch == ' ') {
                continue;
            }

            int value = (int)ch;
            map[value]++;
        }

        boolean foundOdd = false;

        for (int i = 0; i < 128; i++) {
            if (map[i] % 2 != 0) {
                if (foundOdd) {
                    return false;
                } else {
                    foundOdd = true;
                }
            }
        }
        return true;
    }
}
