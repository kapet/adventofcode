import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day03One {

    public static void main(String[] args) {
        var data = new ArrayList<String>();
        try {
            var reader = new BufferedReader(new FileReader("2021/03/input.txt"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                data.add(line.strip());
            }
            reader.close();
        } catch (Exception e) {
            System.out.println(e.getStackTrace());
        }

        int n = data.get(0).length();
        char[] gamma = new char[n];
        char[] epsilon = new char[n];
        for (int i = 0; i < n; i++) {
            var freq = new Counter<String>();
            for (String value : data) {
                freq.add(value.substring(i, i+1));
            }
            int zeros = freq.count("0");
            int ones = freq.count("1");
            if (ones > zeros) {
                gamma[i] = '1';
                epsilon[i] = '0';
            } else {
                gamma[i] = '0';
                epsilon[i] = '1';
            }
        }
        System.out.println(gamma);
        System.out.println(epsilon);
        int gammaInt = Integer.parseInt(new String(gamma), 2);
        int epsilonInt = Integer.parseInt(new String(epsilon), 2);
        System.out.println(gammaInt);
        System.out.println(epsilonInt);
        System.out.println(gammaInt * epsilonInt);
    }
}