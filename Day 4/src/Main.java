import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new File("input.txt"));
        var list = Arrays.stream(scanner.nextLine().split(",")).map(Integer::parseInt).toList();
        scanner.nextLine(); // ignore new line
        var matrixArray = new ArrayList<int[][]>();
        var visitedArray = new ArrayList<boolean[][]>();
        while (scanner.hasNext()) {
            var matrix = new int[5][5];
            for (int i = 0; i < 5; i++) {
                Scanner lsc = new Scanner(scanner.nextLine());
                for (int j = 0; j < 5; j++)
                    matrix[i][j] = lsc.nextInt();
            }
            matrixArray.add(matrix);
            visitedArray.add(new boolean[matrix.length][matrix.length]);
            if (scanner.hasNextLine())
                scanner.nextLine();
        }
        int winCount = 0;
        boolean[] won = new boolean[matrixArray.size()];

        for (int element : list) {
            for (int matrixIndex = 0; matrixIndex < matrixArray.size(); matrixIndex++) {
                if (won[matrixIndex])
                    continue;
                var matrix = matrixArray.get(matrixIndex);
                var visited = visitedArray.get(matrixIndex);
                int n = matrix.length;
                boolean found = false;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (matrix[i][j] == element) {
                            visited[i][j] = true;
                            found = true;
                        }
                    }
                }
                if (!found)
                    continue;
                long sumUnMarked = 0;
                boolean wonGame = false;
                for (int i = 0; i < n; i++) {
                    boolean okRow = true,okColumn = true;
                    for (int j = 0; j < n; j++) {
                        if (!visited[i][j]) {
                            sumUnMarked += matrix[i][j];
                            okRow = false;
                        }
                        if(!visited[j][i])
                            okColumn = false;
                    }
                    if(okColumn || okRow)
                        wonGame = true;
                }
                if (wonGame) {
                    winCount++;
                    won[matrixIndex] = true;
                    if (winCount == matrixArray.size()) {
                        System.out.println(element * sumUnMarked);
                    }
                }
            }
        }
    }
}

