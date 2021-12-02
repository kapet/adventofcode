import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class SolutionTwo {

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("2021/01/input.txt"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                values.add(Integer.valueOf(line));
            }
            reader.close();
        } catch (Exception e) {
            System.out.println(e.getStackTrace());
        }

        int previous = values.get(0) + values.get(1) + values.get(2);
        int increased = 0;
        for (int i = 3; i < values.size(); i++) {
            int v = previous + values.get(i) - values.get(i-3);
            if (v > previous) {
                increased++;
            }
            previous = v;
        }
        System.out.println(increased);
    }
}