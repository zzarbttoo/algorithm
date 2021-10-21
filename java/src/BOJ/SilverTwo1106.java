package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class SilverTwo1106 {

    static final int INF = 987654321;

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringToken = new StringTokenizer(input.readLine(), " ");
        int C = Integer.parseInt(stringToken.nextToken());
        int N = Integer.parseInt(stringToken.nextToken());

        int [] dp = new int[C + 101];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for(int n = 0; n < N; n ++){

            stringToken = new StringTokenizer(input.readLine(), " ");
            int cost = Integer.parseInt(stringToken.nextToken());
            int customer = Integer.parseInt(stringToken.nextToken());

            for(int i = customer; i < C + 101; i ++){
                dp[i] = Math.min(dp[i], cost + dp[i - customer]);
            }
        }

        int answer = INF;
        for(int i = C; i < C + 101 ; i++) answer = Math.min(answer, dp[i]);
        System.out.println(answer);

        }

    }



