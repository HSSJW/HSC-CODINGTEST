import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 1;
        int[] num = new int[5];

        for(int i = 0; i < 5; i++){
            num[i] = sc.nextInt();


        }

        int count = 0;

        while(true){

            count = 0;

            for(int i = 0; i < 5; i++){
                if(max % num[i] == 0){
                    count++;
                }
            }

            if(count >= 3)
                break;

            max++;
        }

        System.out.println(max);
    }

}
