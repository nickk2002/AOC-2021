import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(new File("input.txt"));
        int horizontal = 0;
        int vertical = 0;
        int aim = 0;
        while(scanner.hasNext()){
            String dir = scanner.next();
            int value = scanner.nextInt();
            switch (dir){
                case "forward" -> {
                    horizontal += value;
                    vertical += aim * value;
                }
                case "up" -> aim -= value;
                case "down" -> aim += value;
            }
        }
        System.out.println(horizontal * vertical);
    }
}
