import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        String[] arr = new String[n];

        String result = "";

        for(int i = 0 ; i < n; i++){
            arr[i] = sc.nextLine();
        }

        result =  arr[0]; //첫번째 문장을 저장

        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < result.length() ; j++){

                if(result.charAt(j) != arr[i].charAt(j)){

                    char[] chars = result.toCharArray();

                    chars[j] = '?';

                    result = new String(chars);
                }
            }

        }

        System.out.println(result);
    }
}
