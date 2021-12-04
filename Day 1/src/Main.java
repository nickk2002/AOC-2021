import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input.txt"));
        ArrayList<Integer> list = new ArrayList<>();
        while (scanner.hasNextLine()) {
            list.add(scanner.nextInt());
        }
        int sum = list.get(0) + list.get(1) + list.get(2);
        int index = 0;
        int count = 0;
        for (int i = 3; i < list.size(); i++) {
            int nextSum = sum + list.get(i) - list.get(index);
            if(nextSum > sum){
                count++;
            }
            index++;
        }
        System.out.println(count);
    }
}
