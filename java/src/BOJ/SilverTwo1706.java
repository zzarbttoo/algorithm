package BOJ;

import java.io.*;
import java.util.*;

public class SilverTwo1706 {

    static int R, C;
    static String[] puzzle;

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        puzzle = new String[R];
        ArrayList<String> wordList = new ArrayList<String>();

        for(int i = 0; i < R; i++){
            puzzle[i] = br.readLine();
            st = new StringTokenizer(puzzle[i], "#");

            while(st.hasMoreTokens()){
                String tempString = st.nextToken();
                if (tempString.length() >= 2){
                    wordList.add(tempString);
                }
            }
        }

        for(int i = 0; i < C; i++){
            String temp = "";
            for(int j = 0; j < R; j++){
                temp += puzzle[j].charAt(i);
            }
            st = new StringTokenizer(temp, "#");
            while(st.hasMoreTokens()){
                String tempString = st.nextToken();
                if(tempString.length() >= 2){
                    wordList.add(tempString);
                }
            }
        }

        Collections.sort(wordList);
        //wordList.toString()
        System.out.println(wordList.get(0));





    }
}
