package BOJ;

import java.io.*;
import java.util.*;

public class SilverTwo1325 {

    static int N;
    static int M;
    static Map<Integer, Object> connectMap;
    static int[] connectCount;
    static boolean[] visited;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        connectMap = new HashMap<>();
        connectCount = new int[N + 1];
        visited = new boolean[N + 1];

        for(int i = 1; i < N + 1; i ++){
            connectMap.put(i, new ArrayList<>());
        }

        for(int i = 0 ; i < M; i ++){

            st = new StringTokenizer(br.readLine());

            int firstCom = Integer.parseInt(st.nextToken());
            int secondCom = Integer.parseInt(st.nextToken());

            ArrayList beforeArray = (ArrayList) connectMap.get(secondCom);
            beforeArray.add(firstCom);

            connectMap.put(secondCom, beforeArray);

            //System.out.println(connectMap.get(secondCom).toString());
        }

        for(int i = 1; i < N + 1; i ++){

            if(visited[i] == false){
                dfs(i);
            }

        }


        //System.out.println("connectCount ::: " + Arrays.toString(connectCount));

        int maxNum = -1;
        List maxList = new ArrayList();

        for(int i = 1 ; i < connectCount.length; i ++){
            maxNum = Math.max(maxNum, connectCount[i]);
        }

        for(int j = 1 ; j < connectCount.length; j ++){
            if(connectCount[j] == maxNum){
                maxList.add(j);
            }
        }

        System.out.println(Arrays.toString(connectCount));
        System.out.println(maxList.toString().replaceAll("[^0-9 ]", ""));

    }

    private static void dfs(int start){

        //System.out.println("start ::: " + start);
        //System.out.println("connectMap" +connectMap.get(start).toString());

        for(Object num : (ArrayList) connectMap.get(start)){

            Integer nowNum = (Integer) num;

            //System.out.println("num ::: " + num);
            if(visited[nowNum] == false){
                visited[nowNum] = true;
                dfs(nowNum);
                connectCount[start]++;
            }

        }

        //System.out.println("connectCount ::: " + Arrays.toString(connectCount));


    }
}
