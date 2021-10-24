package BOJ;

import java.io.*;
import java.util.*;

public class SilverTwo1535 {

    static int[][] info;
    static Map<Integer, Integer> numInfo;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int answer = 0;

        info = new int[2][N];
        numInfo = new HashMap<Integer, Integer>();
        numInfo.put(0, 0);

        for(int i = 0; i < 2; i++){
            info[i] = Arrays.asList(br.readLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
        }

        for(int per = 0; per < N; per ++){

            //System.out.println("per ::: " + info[0][per]);
            Map<Integer, Integer> tempHash = new HashMap<Integer, Integer>(numInfo);

            for(Integer key : tempHash.keySet()){
                int tempKey = key + info[0][per];

                //System.out.println("tempKey :: " + tempKey);

                if (tempKey < 100){
                    Integer beforeVal = numInfo.get(tempKey);
                    Integer newVal = numInfo.get(key) + info[1][per];
                    if(beforeVal == null){
                        numInfo.put(tempKey, newVal);
                    }else{
                        numInfo.put(tempKey, Math.max(newVal, beforeVal));
                    }
                }

                for(Integer numKey : numInfo.keySet()){
                    //answer = Math.max(answer, val);
                    if(numKey >= 0 && numKey < 100){
                        answer = Math.max(answer, numInfo.get(numKey));
                    }
                }

            }
        }

        System.out.println(answer);


    }

}
