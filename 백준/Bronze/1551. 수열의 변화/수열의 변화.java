
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();  // 버퍼 비우기

        Integer[] arrA = new Integer[n];
        Integer[] arrB = new Integer[n-1];

        String input = sc.nextLine();
        String[] splitedInput = input.split(",");

        for(int i=0; i < n; i++) {
            arrA[i] = Integer.parseInt(splitedInput[i]);
        }

        for(int i = 0 ; i < k ; i++){

            for(int j = 0 ; j < n-1 ; j++){
                arrB[j] = arrA[j+1] - arrA[j];
                arrA[j]=arrB[j];
            }
        }

        if(k != 0) {
            for (int i = 0; i < n - k; i++) {
                if (i > 0) {
                    System.out.print(",");
                }
                System.out.print(arrB[i]);
            }
        }
        else {
            for (int i = 0; i < n - k; i++) {
                if (i > 0) {
                    System.out.print(",");
                }
                System.out.print(arrA[i]);
            }
        }
    }
}
