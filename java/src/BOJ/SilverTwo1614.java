package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SilverTwo1614 {
    static int finger;
    static Long sickLimit;
    static Long answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Integer.parseInt(br.readLine());
        long sickLimit = Integer.parseInt(br.readLine());

        

        //if (cnt > 0) {
            //if (N % 4 == 1) n += 8 * cnt;
            //else n += cnt / 2 * 8 + cnt % 2 * (8 - (N - 1) * 2);
        //}

    }
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        finger = Integer.parseInt(br.readLine());
//        sickLimit = Long.parseLong(br.readLine());
//        answer = Long.valueOf(0);
//
//        System.out.println(countFinger());
//
//
//    }
//
//
//    static Long countFinger(){
//
//        while(true){
//            //System.out.println(sickCount);
//
//            for(int i = 0 ; i < 5; i ++){
//
//                if(finger == (i + 1)) {
//                    if (sickLimit <= 0) return(answer);
//                    sickLimit--;
//                }
//                answer++;
//                //System.out.println("answer ::: " + answer + "sickLimit ::: " + sickLimit + "i ::: " + i);
//
//            }
//
//            for(int i = 3; i > 0; i--){
//
//                if(finger == (i + 1)){
//                    if (sickLimit <= 0) return(answer);
//                    sickLimit--;
//                }
//                answer++;
//                //System.out.println("answer ::: " + answer + "sickLimit ::: " + sickLimit + "i ::: " + i);
//            }
//        }
//
//    }

}
