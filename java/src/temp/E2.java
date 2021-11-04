package temp;

import java.util.*;
import java.io.*;

public class E2 {

    static int[][] inputArray;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        inputArray = new int[N][3];
        HashMap<Integer, PriorityQueue<Integer>> queueHashMap = new HashMap<Integer, PriorityQueue<Integer>>();

        for(int i = 0; i < N; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            inputArray[i][0] = Integer.parseInt(st.nextToken());
            inputArray[i][1] = Integer.parseInt(st.nextToken());
            inputArray[i][2] = Integer.parseInt(st.nextToken());

            if(queueHashMap.get(inputArray[i][2]) == null)
                queueHashMap.put(inputArray[i][2], new PriorityQueue<Integer>());
        }

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        pq.add(inputArray[0][2]);
        queueHashMap.get(inputArray[0][2]).add(inputArray[0][0]);
        int nowTime = 0;
        int idx = 1;

        while (!pq.isEmpty()){
            int printNum = pq.poll();
            int nowNum = queueHashMap.get(printNum).poll();
            System.out.print(nowNum + " ");
            //System.out.println("inputArray ::: " + Arrays.toString(inputArray[nowNum - 1]));
            nowTime += inputArray[nowNum - 1][1];
            int nextTime = nowTime + inputArray[nowNum - 1][2];

            while(nowTime <= nextTime && idx < N){
                nowTime += 1;
                if (nowTime == inputArray[idx][1]){
                    pq.add(inputArray[idx][2]);
                    queueHashMap.get(inputArray[idx][2]).add(inputArray[idx][0]);
                    idx += 1;
                }
            }

            if(pq.isEmpty() && idx < N){
                pq.add(inputArray[idx][2]);
                queueHashMap.get(inputArray[idx][2]).add(inputArray[idx][0]);
                idx ++;
            }


        }

    }



}
