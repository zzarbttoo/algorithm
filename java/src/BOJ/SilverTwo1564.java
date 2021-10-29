package BOJ;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;


public class SilverTwo1564 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Long N = Long.parseLong(br.readLine());
        BigInteger fact = BigInteger.ONE;
        BigInteger div6 = BigInteger.valueOf(1000000000);
        BigInteger div1 = BigInteger.valueOf(10);
        BigInteger div0 = BigInteger.valueOf(0);


        System.out.println(N);

        System.out.println(Math.floorDiv(N , 2));
        int count = 0;

        for(int i = 1; i < N + 1; i++){
            fact = fact.multiply(BigInteger.valueOf(i));


            while(fact.remainder(div6).equals(div6)){
                fact = fact.divide(div6);
                //count ++;
                //System.out.println(count);
            }

            while(fact.remainder(div1).equals(div0)){

                fact = fact.divide(div1);
                //count ++;
                //System.out.println(count);
            }

        }

        System.out.println(fact);


//        for(Long i = Long.valueOf(1); i <= Math.floorDiv(N , 2); i ++){
//            System.out.println(i);
//            System.out.println(N - i + 1);
//        }


    }
}
