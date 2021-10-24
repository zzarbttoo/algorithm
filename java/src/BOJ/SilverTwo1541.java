package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SilverTwo1541 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), "-");

        int count = 0;
        int answer = 0;

        while(st.hasMoreTokens()){

            if(count == 0){
                StringTokenizer plusSt = new StringTokenizer(st.nextToken(), "+");

                while(plusSt.hasMoreTokens()){
                    answer += Integer.parseInt(plusSt.nextToken());
                    //System.out.println("answer ::: " + answer);
                }
            }else{

                //System.out.println(st.nextToken());
                StringTokenizer plusSt = new StringTokenizer(st.nextToken(), "+");

                while(plusSt.hasMoreTokens()){
                    answer -= Integer.parseInt(plusSt.nextToken());
                }

            }

            count++;

        }

        System.out.println(answer);

    }
}
