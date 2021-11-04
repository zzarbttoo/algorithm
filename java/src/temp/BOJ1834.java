package temp;

import java.io.*;

public class BOJ1834 {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Integer.parseInt(br.readLine());
        long answer = 0;


        for(long i = 0; i < N; i++){
            answer += N * i + i;
        }

        System.out.println(answer);



    }
}
