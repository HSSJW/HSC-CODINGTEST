
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int count = 0;

        if(b>=c) //손익분기점이 발생하지않는 경우
            System.out.println(-1);
        else{
            int extra = c - b;

            while(a >= 0){
                a -= extra;
                count++;
            }

            System.out.println(count);
        }
    }
}
