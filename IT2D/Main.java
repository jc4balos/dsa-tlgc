package IT2D;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scn1 = new Scanner(System.in);
        System.out.print("Number of Students");
        int studentNo = Integer.parseInt(scn1.nextLine());

        String[] names = new String[studentNo];
        Scanner scn = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            System.out.print("Name: ");
            names[i] = scn.nextLine();
        }

    }
}