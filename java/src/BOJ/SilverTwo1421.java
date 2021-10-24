package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SilverTwo1421 {

    static int N, C, W;
    static int[] trees;

    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        trees = new int[N];
        int maxNum = -1;

        for(int i = 0; i < N; i ++){
            trees[i] = Integer.parseInt(br.readLine());
            maxNum = Math.max(maxNum, trees[i]);
        }

        int answer = -1;

        //길이만큼 반복
        for(int tLen = 1; tLen <= maxNum; tLen++){

            int sum = 0;

            for(int treeIdx = 0; treeIdx < N; treeIdx++){

                if(trees[treeIdx] >= tLen){

                    int treeNumber = Math.floorDiv(trees[treeIdx], tLen);
                    int last = Math.floorMod(trees[treeIdx], tLen);
                    int minus = 0;

                    if (last == 0){
                        minus = treeNumber - 1;
                    }else{
                        minus = treeNumber;
                    }
                    //sum += (treeNumber * tLen * W) - minus * C;
                    int addNum = (treeNumber * tLen * W) - minus * C;
                    if (addNum > 0){
                        sum += addNum;
                    }
                }

                //System.out.println("sum ::: " + sum);
            }
            answer = Math.max(answer, sum);

        }

        System.out.println(answer);




    }
}
