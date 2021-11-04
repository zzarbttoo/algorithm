package temp;

import java.io.*;
import java.util.*;

public class E3 {
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] startX = new int[N];
        int[] widthAdd = new int[N];

        int temp = 0;

        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            if (i == 0) widthAdd[i] += w * h;
            else widthAdd[i] += w * h + widthAdd[i-1];

            startX[i] = temp;
            temp += w;

        }

        System.out.println(Arrays.toString(widthAdd));

        //시작점
        for(int i = 0; i < N - 2; i ++){
            //끝점
            for(int j = i + 2; j < N; j++){
                System.out.println("i ::: " + i + " j :::" + j);
            }
        }

    }
}
