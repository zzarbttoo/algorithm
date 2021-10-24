package BOJ;

import java.io.*;
import java.util.*;

public class SilverTwo1260 {

    private static int N, M, V;
    private static boolean[] visitedBFS;
    private static boolean[] visitedDFS;
    private static int[][] connected;
    private static List<Integer> answerBFS;
    private static List<Integer> answerDFS;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringToken = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(stringToken.nextToken());
        M = Integer.parseInt(stringToken.nextToken());
        V = Integer.parseInt(stringToken.nextToken());

        //System.out.println("N ::: " + N + " M ::: " + M + " v ::: " + V);

        //int[][] nodeArray = new int[M][2];
        connected = new int[N + 1][N + 1];
        answerBFS = new ArrayList<Integer>();
        answerDFS = new ArrayList<Integer>();

        visitedBFS = new boolean[N + 1];
        visitedDFS = new boolean[N + 1];

        for(int i = 0; i < M; i++){

            //nodeArray[i] = Arrays.asList(br.readLine().split(" "))
            //.stream().mapToInt(Integer::parseInt).toArray();
            stringToken = new StringTokenizer(br.readLine() , " ");
            int start = Integer.parseInt(stringToken.nextToken());
            int end = Integer.parseInt(stringToken.nextToken());

            //양방향
            connected[start][end] = 1;
            connected[end][start] = 1;

        }

        bfs(V);
        dfs(V);

        //System.out.println(Arrays.toString(answerDFS.stream().mapToInt(i -> i).toArray()));
        //System.out.println(Arrays.toString(answerBFS.stream().mapToInt(i -> i).toArray()));

        System.out.println(answerDFS.toString().replaceAll("[^0-9 ]", ""));
        System.out.println(answerBFS.toString().replaceAll("[^0-9 ]", ""));


    }

    public static void bfs(int nowNode){

        LinkedList<Integer> queue = new LinkedList<>();
        queue.offer(nowNode);

        visitedBFS[nowNode] = true;
        answerBFS.add(Integer.valueOf(nowNode));

        while(! queue.isEmpty()){

            int popNum = queue.poll();

            for(int i = 1 ; i <= N ; i ++){
                if (connected[popNum][i] == 1 && visitedBFS[i] == false){
                    queue.offer(i);
                    visitedBFS[i] = true;
                    answerBFS.add(Integer.valueOf(i));

                }
            }
        }
    }

    public static void dfs(int nowNode){

        visitedDFS[nowNode] = true;
        answerDFS.add(nowNode);


        for(int i = 1; i <= N; i ++ ){
            if(connected[nowNode][i] == 1 && visitedDFS[i] == false){
                dfs(i);
            }
        }

    }
}
