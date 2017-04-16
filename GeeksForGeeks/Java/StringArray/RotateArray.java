package Java.StringArray;

/**
 * @author: Arnav Garg
 */

/*
* Rotate an array of n elements to the right by k steps.
* For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
*
* Solutions:
* -we divide the array into two parts [1,2,3,4 || 5,6,7] and reverse part 1 [4,3,2,1,5,6,7] and then we reverse
* second part [4,3,2,1,7,6,5] and then we just reverse the entire array [5,6,7,1,2,3,4]
* */
public class RotateArray {

    public void rotateArray(int[] arr, int k) {

        int length = arr.length;
        reverse(arr, 0, length-k-1);
        reverse(arr, k+1, length-1);
        reverse(arr, 0, length-1);

        //printing array
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public void reverse(int[] arr, int start, int end) {

        while(start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            end--;
            start++;
        }

    }
}
