import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean find = false;

        for(int i=0; i < 5; i++){
            String input = sc.nextLine();

            if(input.contains("FBI")){
                find = true;
                System.out.print(i+1 + " ");
            }
        }

        if(!find)
            System.out.println("HE GOT AWAY!");

    }
}
