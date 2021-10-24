package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SilverTwo1455 {


    static int N, M;
    static int[][] before;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        before = new int[N][M];

        for(int i = 0; i < N; i++){
            before[i] = Arrays.asList(br.readLine().split("")).stream().mapToInt(Integer::parseInt).toArray();
        }

        int count = 0;

        for(int i = N - 1; i >= 0; i--){
            for(int j = M - 1; j >= 0; j --){
                //System.out.println(before[i][j]);

                if (before[i][j] == 1){
                    count += 1;
                    for(int y = 0; y <= i; y ++){
                        for(int x = 0; x <= j; x++){
                            if(before[y][x] == 0){
                                before[y][x] = 1;
                            }else{
                                before[y][x] = 0;
                            }
                        }
                    }
                }
            }
        }

        System.out.println(count);

        //for(int[] array : before){
            //System.out.println(Arrays.toString(array));
        //}




    }
}
