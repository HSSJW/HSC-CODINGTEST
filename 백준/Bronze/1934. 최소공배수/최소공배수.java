import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for(int i = 0; i < t; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            int lcm = lcm(a, b);
            System.out.println(lcm);
        }

        scanner.close();
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }

    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

}
