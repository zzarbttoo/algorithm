package BOJ;

import java.io.*;
import java.util.*;


public class SilverTwo1497 {

    static int N, M;
    static long[] guiter;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        guiter = new long[N];

        for(int i = 0; i < N; i ++){

            String temp = br.readLine().split(" ")[1];

            for(int j = 0; j < M; j ++){
                if(temp.charAt(j) == 'Y'){
                    guiter[j] |= (1 << (M - 1 - j));
                }
            }
        }

        //dfs(0, 0, 0);
    }



}
//    static int N, M;
//    static String[] guitar;
//    static int[] possible;
//    static HashMap<Integer, Integer> countHash;
//    static int max;
//
//
//    public static void main(String[] args) throws Exception{
//
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        N = Integer.parseInt(st.nextToken());
//        M = Integer.parseInt(st.nextToken());
//        guitar = new String[N];
//        possible = new int[N];
//        countHash = new HashMap<Integer, Integer>();
//        max = -1;
//
//        for(int i = 0; i < N; i ++){
//                st = new StringTokenizer(br.readLine());
//            guitar[i] = st.nextToken();
//            String temp = st.nextToken();
//            String binString = "";
//
//            for(char ch : temp.toCharArray()){
//                if(ch == 'Y') binString += '1';
//                else binString += '0';
//            }
//
//            possible[i] = Integer.parseInt(binString, 2);
//
//        }
//
//        dfs(0, 0, 0);
//
//        if (max == -1) System.out.println(-1);
//        else System.out.println(countHash.get(max));
//
//
//
//    }
//
//    static void dfs(int before, int bit, int count){
//
//        //if (bit == answerWord) min = Math.min(min, count);
//        if (max <= bit){
//            max = bit;
//            if (countHash.get(max) == null) countHash.put(max, count);
//            else {
//                countHash.put(max, Math.min(countHash.get(max), count));
//            }
//        }
//
//        for(int i = before + 1; i < N; i++){
//            int tempBit = bit;
//            tempBit |= possible[i];
//
//            dfs(i, tempBit, count + 1);
//        }
//
//    }
//
//}