import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {


        int n, m;
        int[][] coins;
        int count = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        coins = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();

            for(int j = 0; j < m ; j++){
                coins[i][j] = line.charAt(j) - '0';
            }
        }


        for (int i = n-1; i >= 0; i--){
            for (int j = m-1; j >= 0; j--){

                if(coins[i][j] == 1){
                    for (int k = 0; k <= i; k++) {
                        for (int l = 0; l <= j; l++) {
                            // 0은 1로, 1은 0으로 변경
                            coins[k][l] = 1 - coins[k][l];
                        }
                    }

                    count++;
                }
            }
        }

        System.out.println(count);
    }
}