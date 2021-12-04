import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.function.BiPredicate;

public class Main {
    public static int solveFor(ArrayList<Integer> numbers, int length, BiPredicate<Integer,Integer> comp){
        int max = (int)Math.pow(2,length - 1);
        ArrayList<Integer> currentElements = new ArrayList<>(numbers);
        for(int i = max; i >= 0 && currentElements.size() > 1; i /= 2) {
            int count1 = 0,count0 = 0;
            for (int element : currentElements) {
                if ((element & i) > 0) {
                    count1++;
                } else
                    count0++;
            }
            final boolean value = comp.test(count0, count1);
            final int index = i;
            currentElements.removeIf((element) -> {
                boolean bit = ((element & index) > 0);
                return (bit != value);
            });
        }
        return currentElements.get(0);
    }
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input.txt"));
        ArrayList<Integer> numbers = new ArrayList<>();
        int length = 0;
        while(scanner.hasNext()){
            String base2 = scanner.next();
            length = base2.length();
            int number = Integer.parseInt(base2,2);
            numbers.add(number);
        }
        int oxygen = solveFor(numbers, length, (count0, count1) -> count1 >= count0);
        int carbon = solveFor(numbers, length, (count0, count1) -> count1 < count0);

        System.out.println(oxygen + " " + carbon);
        System.out.println(oxygen * carbon);
    }
}
