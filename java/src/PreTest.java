import java.util.*;

public class PreTest {

    private static int[][] visited;
    private static List<Integer> visitNum;
    private static int countNum;


    private static void setVisited(int sizeOfMatrix){
        visited = new int[sizeOfMatrix][sizeOfMatrix];
    }

    private static void setVisitNum(){
        visitNum = new ArrayList<Integer>();
    }

    private static void solution(int sizeOfMatrix, int[][] matrix){

        int count = 0;
        String answer = "";
        List<Integer> sortList = new ArrayList<Integer>();

        setVisited(sizeOfMatrix);
        setVisitNum();


        for(int r = 0; r < sizeOfMatrix; r++){
            for (int c = 0; c < sizeOfMatrix; c ++){
                if(matrix[r][c] == 1 && visited[r][c] == 0){
                    count += 1;
                    countNum = 0;
                    countNum ++;

                    search(r, c, sizeOfMatrix, matrix);
                    sortList.add(countNum);
                }
            }
        }

        Collections.sort(sortList);
        answer = sortList.toString().replaceAll("[^0-9 ]", "");

        System.out.println(count);

        if(count > 0) {
            System.out.println(answer);
        }
    }

    private static void search(int nowX, int nowY, int sizeOfMatrix, int[][] matrix){

        int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        visited[nowX][nowY] = -1;

        for (int [] direct : direction){
            int nextX = nowX + direct[0];
            int nextY = nowY + direct[1];

            if (nextX >= 0 && nextX < sizeOfMatrix && nextY >= 0 && nextY < sizeOfMatrix && matrix[nextX][nextY] == 1){
                countNum ++;
                search(nextX, nextY, sizeOfMatrix, matrix);

            }
        }
    }




}

