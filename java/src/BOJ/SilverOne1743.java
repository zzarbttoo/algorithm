package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Boolean.TRUE;

public class SilverOne1743 {

    static int N, M, K;
    static Boolean[][] trash;
    static Boolean[][] visited;
    static int answer;
    static int count;
    static int[][] direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        trash = new Boolean[N][M];
        visited = new Boolean[N][M];
        answer = 0;
        count = 0;

        for(int i = 0; i < K; i++){
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken()) - 1;
            trash[y][x] = TRUE;
        }

        for(int y = 0; y < N; y ++){
            for(int x = 0; x < M; x++){
                if (visited[y][x] == null){
                    count = 0;
                    visited[y][x] = TRUE;
                    dfs(y, x);
                }
                if (answer < count){
                    answer = count;
                }
            }
        }

        System.out.println(answer);
    }

    public static void dfs(int y, int x){
        if(trash[y][x] == TRUE){
            count++;
            for (int[] d : direction) {
                int ny = y + d[0];
                int nx = x + d[1];
                if(0 <= ny && ny < N && 0 <= nx && nx < M && visited[ny][nx] == null){
                    visited[ny][nx] = TRUE;
                    dfs(ny, nx);
                }
            }
        }
    }


}
