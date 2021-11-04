package temp;

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class BOJ1766 {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        List<List<Integer>> childArray = new ArrayList<List<Integer>>();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int [] countArray = new int[N + 1];
        List<Integer> answerList = new ArrayList<Integer>();


        for(int i = 0; i < N + 1; i++) childArray.add(new ArrayList<Integer>());
        //System.out.println(childArray.toString());

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int before = Integer.parseInt(st.nextToken());
            int after = Integer.parseInt(st.nextToken());

            childArray.get(before).add(after);
            countArray[after] ++;
        }

        for(int i = 1; i < N + 1; i ++) {
            if(countArray[i] == 0) pq.add(i);
        }


        while(!pq.isEmpty()){
            int now = pq.poll();
            System.out.print(now + " ");

            answerList.add(now);

            for(Integer child : childArray.get(now)){

                countArray[child]--;
                if(countArray[child] == 0) pq.add(child);
            }
        }


        //System.out.println(answerList.stream().map(String::valueOf).collect(Collectors.joining(" ")));




    }
}
