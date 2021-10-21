package BOJ;

import java.io.*;
import java.util.*;

public class SilverTwo1206 {

    static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        Double[] avgNum = new Double[N];
        int[] littleNum = new int[N];
        Arrays.fill(littleNum, 1);

        for(int i = 0 ; i < N ; i ++){
            avgNum[i] = Double.parseDouble(br.readLine());
            while(true){
                Double tempValue = avgNum[i] * littleNum[i];

                System.out.println("littleNum" + littleNum[i]);
                System.out.println("tempValue ::: " + tempValue);


                if (tempValue.intValue() == tempValue){
                    break;
                }else{
                    littleNum[i] ++;
                }

            }
        }

        //System.out.println(Arrays.toString(avgNum));
        //System.out.println(Arrays.toString(littleNum));

        int answer = 0;

        for(int i = 0; i < N; i ++){
            answer = gcd(Math.max(littleNum[i], answer), Math.min(littleNum[i], answer));
        }

        System.out.println(answer);


    }


    public static int gcd(int a, int b){


        if (b == 0) return a;
        return gcd(a, a % b);
    }

}
