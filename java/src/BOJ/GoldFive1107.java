package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class GoldFive1107 {

    static int N, M;
    static HashMap<Character, Boolean> er;
    static int[] memo;
    static boolean[] isErr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());


        er = new HashMap<>();

        if (N <= 100) {
            memo = new int[101];
            isErr = new boolean[101];
        }
        else{
            memo = new int[2 * N + 1];
            isErr = new boolean[2 * N + 1];
        }

        memo[100] = 0;

        for(int i = 0; i <= 9; i++){
            er.put(Integer.toString(i).charAt(0), false);
        }

        if(M != 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0; i < M ; i ++){
                er.put(st.nextToken().charAt(0), true);
            }
        }

        if (N == 100){
            System.out.println(0); //정답 출력
        }


        if(N < 100){
            for(int i = 99; i >= 0; i --){
                String now = Integer.toString(i);
                for(int j = 0; j < now.length(); j++){
                    if(er.get(now.charAt(j))){
                        isErr[i] = true;
                        break;
                    }
                }
                if(!isErr[i] && (memo[i + 1] + 1 > now.length())){
                    memo[i] = now.length();
                }else{
                    memo[i] = memo[i + 1] + 1;
                }
            }

            for(int i = 1; i <= N; i ++){
                if(memo[i - 1] + 1 < memo[i]){
                    memo[i] = memo[i - 1] + 1;
                }
            }

            System.out.println(memo[N]); //정답 출력
        }

        if(N > 100){
            for(int i = 101; i <= 2 * N; i ++){
                String now = Integer.toString(i);
                for(int j = 0; j < now.length(); j++){
                    if(er.get(now.charAt(j))){
                        isErr[i] = true;
                        break;
                    }
                }

                if(!isErr[i] && (memo[i - 1] + 1 > now.length())){
                    memo[i] = now.length();
                }else{
                    memo[i] = memo[i - 1] + 1;
                }
            }

            for(int i = 2 * N - 1; i >= 100; i --){
                if (memo[i + 1] + 1 < memo[i]){
                    memo[i] = memo[i + 1] + 1;
                }
            }

            System.out.println(memo[N]);
        }
    }
}
