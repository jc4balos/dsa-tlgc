package training;

import java.util.ArrayList;

public class Main {
    public static boolean isPalindrome(int x) {
        String num = Integer.toString(x); // cinovert to string
        String[] arr1 = num.split(""); // nilagay sa array ung x

        // gumawa ng bagong arraylist (paglalagyan ng nakabaligtad)
        ArrayList<String> arrReverse = new ArrayList<String>();

        // [1,2,3]
        // sinalpak yung nakabaligtad sa arraylist na ginawa kanina
        for (int i = arr1.length - 1; i > 0; i--) {
            arrReverse.add(arr1[i]);
        }

        // check kung magkapareho ung value kada index
        for (int j = 0; j < arr1.length; j++) {
            if (arr1[j] == arrReverse.get(j)) {
                continue;
            } else {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        System.out.print(isPalindrome(123));
    }

}