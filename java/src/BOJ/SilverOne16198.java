package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SilverOne16198 {

    static int N;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        ArrayList<Integer> W = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        answer = 0;

        for(int n = 0; n < N; n++){
            W.add(Integer.parseInt(st.nextToken()));
        }

        dfs(W, 0);

        System.out.println(answer);
    }

    public static void dfs(ArrayList<Integer> W, int before){

        if(W.size() > 2){
            for(int i = 1; i < W.size() - 1; i++){
                int energy = W.get(i - 1) * W.get(i + 1);
                if(before + energy > answer){
                    answer = before + energy;
                }
                int delNum = W.remove(i);

                dfs(W, before + energy);
                W.add(i, delNum); //복구
            }
        }
    }
}
