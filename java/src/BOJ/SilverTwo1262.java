package BOJ;

import java.util.*;
import java.io.*;

public class SilverTwo1262 {

    private static int N, R1, C1, R2, C2;
    private static ArrayList<String> diamond;
    private static char[] alpha;

    private static String diaMaker(int i){

        String makeString = "";

        //System.out.print(".".repeat(N - i));
        makeString += ".".repeat(N-i);

        for(int j = 0; j < i; j ++){
            //System.out.print(alpha[N - (j + 1)]);
            makeString += alpha[N-(j +1)];
        }
        for(int j = i - 1; j > 0; j --){
            //System.out.print(alpha[N - j]);
            makeString += alpha[N - j];
        }

        //System.out.print(".".repeat(N - i));

        makeString += ".".repeat(N-i);

        return makeString;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        N = Integer.parseInt(tokenizer.nextToken());
        R1 = Integer.parseInt(tokenizer.nextToken());
        C1 = Integer.parseInt(tokenizer.nextToken());
        R2 = Integer.parseInt(tokenizer.nextToken());
        C2 = Integer.parseInt(tokenizer.nextToken());

        alpha = new char[26];

        for(int i = 0; i < 26; i ++){
            alpha[i] = (char)(97 + i);
        }

        System.out.println(Arrays.toString(alpha));

        diamond = new ArrayList<>();

        System.out.println("start ::: " + alpha[N - 1]);

        for(int i = 1; i < N + 1; i ++){
            diamond.add(diaMaker(i));
        }
        for(int i = N - 1; i > 0; i-- ){
            diamond.add(diaMaker(i));
        }

        System.out.println(diamond.indexOf(3));




    }
}
