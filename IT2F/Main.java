public class Main {
    public static void main(String[] args) {
        String[] names = new String[10];
        int[] ages = { 23, 42, 22, 33, 41 };

        System.out.println(ages[2]);
        names[6] = "Arjones";
        names[4] = "Discaya";
        names[1] = "Torre";

        for (int i = 0; i <= 9; i++) {
            System.out.println(names[i]);
        }
    }
}
