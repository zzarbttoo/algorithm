package BOJ;

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Tomato{
    int y;
    int x;

    Tomato(int y, int x){
        this.y = y;
        this.x = x;
    }

}
public class GoldFive7576 {

    static int M, N;
    static int[][] B;
    static Boolean[][] V;
    static int[][] direction = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    static Queue<Tomato> que;
    static int zCount;



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        B = new int[N][M];
        V = new Boolean[N][M];
        zCount = 0;
        que= new LinkedList<Tomato>();

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());

            for(int j = 0; j < M; j++){
                B[i][j] = Integer.parseInt(st.nextToken());
                if (B[i][j] == 0) zCount += 1;
                if (B[i][j] == 1) que.add(new Tomato(i, j));
            }
        }

        int tempCount;
        int time = 0;

        while (!que.isEmpty()){
            tempCount = que.size();
            for(int i = 0; i < tempCount; i ++){
                Tomato now = que.poll();
                for(int[] d : direction){
                    int ny = now.y + d[0];
                    int nx = now.x + d[1];

                    if(0 <= ny && ny < N && 0 <= nx && nx < M){
                        if(B[ny][nx] == 0){
                            zCount -= 1;
                            B[ny][nx] = 1;
                            que.add(new Tomato(ny, nx));
                        }
                    }
                }
            }
            time += 1;
        }

        if (zCount == 0){
            System.out.println(time - 1);
        }else{
            System.out.println(-1);
        }

    }


}
