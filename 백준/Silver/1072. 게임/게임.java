import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double x = sc.nextInt(); //게임횟수
        double y = sc.nextInt(); //이긴게임

        double z = y*100/x; // 승률 >> INT형이므로 소수점은 버려짐
        z = (int) z;

        double newZ;
        int result = 0;


        if(z >= 99){ //절대 안변하는 경우
            System.out.println("-1");
        }
        else {
            while(true){
                x += 1;
                y += 1;
                newZ = y*100/x;
                newZ = (int) newZ; //소수점 제거
                result++;

                if(newZ > z){
                    System.out.println(result);
                    break;
                }
            }
        }
    }
}
