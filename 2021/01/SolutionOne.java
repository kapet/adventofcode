import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

/**
 * SolutionOne
 */
public class SolutionOne {

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("01/input.txt"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                values.add(Integer.valueOf(line));
            }
            reader.close();
        } catch (Exception e) {
            System.out.println(e.getStackTrace());
        }

        int previous = values.get(0);
        int increased = 0;
        for (int i = 1; i < values.size(); i++) {
            int v = values.get(i);
            if (v > previous) {
                increased++;
            }
            previous = v;
        }
        System.out.println(increased);
    }
}