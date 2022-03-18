package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Color{
    int y, x;

    Color(int y, int x){
        this.y = y;
        this.x = x;
    }
        }

public class GoldFive10026 {
    static boolean[][] visN, visAb;
    static int N;
    static Character[][] color;
    static int cntN = 0;
    static int cntAb = 0;
    static int[][] direction = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

         color = new Character[N][N];
         visN= new boolean[N][N];
         visAb= new boolean[N][N];

        for(int i = 0; i < N; i++){

            String str = br.readLine();
            int j = 0;

            for(Character st : str.toCharArray()){
                color[i][j] = st;
                visN[i][j] = false;
                visAb[i][j] = false;
                j += 1;
            }
        }

        for(int i = 0; i < N; i++){
            for(int j= 0; j < N; j++){
                if(!visN[i][j]){
                    cntN += 1;
                    visN[i][j] = true;
                    dfsN(new Color(i, j));
                }

                if(!visAb[i][j]){
                    cntAb += 1;
                    visAb[i][j] = true;
                    dfsAb(new Color(i, j));
                }
            }
        }

        System.out.print(cntN + " " + cntAb);

    }



    //normal
    static void dfsN(Color co){

        for(int[] d: direction){
            int ny = co.y + d[0];
            int nx = co.x + d[1];

            if(0 <= ny && ny < N && 0 <= nx && nx < N){
                if(!visN[ny][nx] && color[co.y][co.x] == color[ny][nx]){
                    visN[ny][nx] = true;
                    dfsN(new Color(ny, nx));
                }
            }
        }
    }

    //abnormal
    static void dfsAb(Color co){

        for(int[] d: direction){
            int ny = co.y + d[0];
            int nx = co.x + d[1];

            if(0 <= ny && ny < N && 0 <= nx && nx < N && !visAb[ny][nx]){
                if((color[co.y][co.x].equals('R') || color[co.y][co.x].equals('G'))
                        && (color[ny][nx].equals('R') || color[ny][nx].equals('G'))){
                    visAb[ny][nx] = true;
                    dfsAb(new Color(ny, nx));
                }
                else if(color[co.y][co.x].equals('B') && color[ny][nx].equals('B')){
                    visAb[ny][nx] = true;
                    dfsAb(new Color(ny, nx));
                }

            }
        }
    }


}
