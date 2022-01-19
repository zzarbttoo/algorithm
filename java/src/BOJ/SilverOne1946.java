package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class SilverOne1946 {


    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static int solution() throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());

        int person = Integer.parseInt(st.nextToken());
        int[][] order = new int[person][2];
        int[] keyArray = new int[2];
        int count = 0;

        for(int i = 0; i < person; i ++){
            st = new StringTokenizer(br.readLine());
            order[i] = new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        Arrays.sort(order, Comparator.comparingInt(num -> num[0]));

        if(order.length > 0){
            keyArray = order[0];
        }

        for (int[] inner: order) {
            if (inner[1] <= keyArray[1]){
                count += 1;
                keyArray = inner;
            }
        }

        return count;

}

    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());

        int round= Integer.parseInt(st.nextToken());
        int answer[] = new int[round];

        for(int i = 0; i < round; i ++){
            answer[i] = solution();
        }

        for (int a:answer) {
            System.out.println(a);
        }
    }

}
