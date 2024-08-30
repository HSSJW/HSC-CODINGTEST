import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        long n = sc.nextInt();
        long a = 0;
        long b = 0;
        long result = 0;

        for(long i = n;; i++){
            a = i / n; //몫
            b = i % n; //나머지

            if(a == b){
                result += i;
                i+=n;
            }

            if(n*n <= i)
                break;
        }

        System.out.println(result);
    }
}
