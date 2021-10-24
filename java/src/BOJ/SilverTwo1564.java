package BOJ;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;


public class SilverTwo1564 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Long N =Long.parseLong(br.readLine());
        BigInteger fact = BigInteger.valueOf(1);
        BigInteger modNum1 = BigInteger.valueOf(10);
        BigInteger modNum2 = BigInteger.valueOf(100);
        BigInteger modNum3 = BigInteger.valueOf(1000);
        BigInteger modNum4 = BigInteger.valueOf(10000);
        BigInteger modNum5 = BigInteger.valueOf(100000);
        BigInteger modNum6 = BigInteger.valueOf(1000000);

        BigInteger lastNum = BigInteger.valueOf(0);

        //int halfN = Math.floorDiv(N, 2);
        //int last = Math.floorMod(N, 2);

        for(Long i = Long.valueOf(1); i < N; i++){
            fact = fact.multiply(BigInteger.valueOf(i));
           }

        System.out.println(fact);




        }



        //StringBuffer factNum = new StringBuffer(BigInteger.);
        //String tempStr = factNum.reverse().toString();

        //Long reversNum = Long.parseLong(tempStr);
        //String reverseStr = Long.toString(reversNum);
        //String answer = "";

        //System.out.println(reverseStr);

        //for(int i = 4; i >= 0; i --){
            //answer += reverseStr.charAt(i);
        //}

        //System.out.println(answer);

    }
