import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int count = scanner.nextInt();
            int ball = 1;
            boolean[] arr = new boolean[3];
            arr[0] = true;
            int a;
            int b;

            for(int i = 0; i < count; i++){
                a = scanner.nextInt();
                b = scanner.nextInt();

                if(arr[a-1]){
                    arr[a-1] = false;
                    arr[b-1] = true;
                }
                else if (arr[b-1]){
                    arr[a-1] = true;
                    arr[b-1] = false;
                }
            }


            if(arr[0]){
                System.out.println("1");
            }
            else if(arr[1]){
                System.out.println("2");
            }
            else if(arr[2]){
                System.out.println("3");
            }

        }

}
