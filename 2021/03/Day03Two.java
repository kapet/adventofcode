import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day03Two {

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

        var oxyData = new ArrayList<String>(data);
        for (int i = 0; i < n; i++) {
            var freq = new Counter<String>();
            for (String value : oxyData) {
                freq.add(value.substring(i, i+1));
            }
            int zeros = freq.count("0");
            int ones = freq.count("1");
            char keep = '0';
            if (ones >= zeros) {
                keep = '1';
            }
            var newOxyData = new ArrayList<String>();
            for (String value : oxyData) {
                if (value.charAt(i) == keep) {
                    newOxyData.add(value);
                }
            }
            oxyData = newOxyData;
            if (oxyData.size() <= 1) {
                break;
            }
        }

        var co2Data = new ArrayList<String>(data);
        for (int i = 0; i < n; i++) {
            var freq = new Counter<String>();
            for (String value : co2Data) {
                freq.add(value.substring(i, i+1));
            }
            int zeros = freq.count("0");
            int ones = freq.count("1");
            char keep = '0';
            if (ones < zeros) {
                keep = '1';
            }
            var newCo2Data = new ArrayList<String>();
            for (String value : co2Data) {
                if (value.charAt(i) == keep) {
                    newCo2Data.add(value);
                }
            }
            co2Data = newCo2Data;
            if (co2Data.size() <= 1) {
                break;
            }
        }

        System.out.println(oxyData.get(0));
        System.out.println(co2Data.get(0));
        int oxyInt = Integer.parseInt(oxyData.get(0), 2);
        int co2Int = Integer.parseInt(co2Data.get(0), 2);
        System.out.println(oxyInt);
        System.out.println(co2Int);
        System.out.println(oxyInt * co2Int);
    }
}