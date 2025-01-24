import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String input = br.readLine();

        int i = Integer.parseInt(br.readLine());

        i -= 1;

        System.out.println(input.charAt(i));
    }
}
