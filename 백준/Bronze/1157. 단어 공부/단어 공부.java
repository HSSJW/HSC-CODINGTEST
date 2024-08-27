import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);


        int[] alpha = new int[26];
        String input = sc.nextLine(); //문자열 입력받음

        for(int i = 0 ; i < input.length() ; i++){
            if(input.charAt(i) >= 'a' && input.charAt(i) <= 'z'){ //소문자
                alpha[input.charAt(i) - 'a']++;
            }
            else{ //대문자
                alpha[input.charAt(i) - 'A']++;
            }
        }

        int max = -1;
        char result = ' ';

        for(int i = 0 ; i < 26; i++){
            if(alpha[i] > max){
                max = alpha[i];
                result = ((char)(i+'A'));
                //index번호를 다시 알파벳으로
            }
            else if(alpha[i] == max){
                result = '?';
                
            }
        }
        
        System.out.println(result);

    }
}
