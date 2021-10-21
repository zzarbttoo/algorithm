package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SilverTwo1182 {

    static int[] numArray;
    static int N;
    static int S;
    static int count;

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringToken = new StringTokenizer(input.readLine(), " ");

        count = 0;

        N = Integer.parseInt(stringToken.nextToken());
        S = Integer.parseInt(stringToken.nextToken());


        numArray = Arrays.asList(input.readLine().split(" "))
                .stream().mapToInt(Integer::parseInt).toArray();

        //System.out.println("numArray ::: " + Arrays.toString(numArray));


        //backTrack( );

        for(int i = 0; i < N ;i ++){

            if(numArray[i] == S){
                //System.out.println(numArray[i]);
                count ++;
            }

            //System.out.println("i ::: " + i);

            backTrack(i, numArray[i]);
        }


        System.out.println(count);
    }


    public static void backTrack(int beforeStartIdx, int beforeSum){

        //System.out.println("beforeSum ::: " + beforeSum);

            for(int nowIdx = beforeStartIdx + 1; nowIdx < N; nowIdx ++){
                int nowSum = numArray[nowIdx] + beforeSum;
                //System.out.println("nowSum ::: " + nowSum);

                if(nowSum == S){
                    count ++;
                }

                backTrack(nowIdx, nowSum);
        }
    }



}
