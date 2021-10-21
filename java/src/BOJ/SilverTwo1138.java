package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SilverTwo1138 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int number = Integer.parseInt(br.readLine());
        //System.out.println(number);

        int[] numArray = Arrays.asList(br.readLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
        //System.out.println(Arrays.toString(numArray));

        int start = 0;
        int end = number - 1;

        //int[] answer = new int[number];
        //Arrays.fill(answer, 0);

        List<Integer> list = new ArrayList<>();

        for(int i = end; start <= i; i-- ){
            //list.add(numArray[i]);
            //System.out.println(numArray[i]);
            list.add(numArray[i], i + 1);
        }

        System.out.println(list.toString().replaceAll("[^0-9 ]", ""));





    }

}

