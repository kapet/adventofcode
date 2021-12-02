import java.io.BufferedReader;
import java.io.FileReader;

public class One {

    public static void main(String[] args) {
        int h = 0;
        int v = 0;

        try {
            BufferedReader reader = new BufferedReader(new FileReader("2021/02/input.txt"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                String[] lineSplit = line.split(" ");
                int dist = Integer.parseInt(lineSplit[1]);
                switch (lineSplit[0]) {
                    case "forward":
                        h += dist;
                        break;
                
                    case "up":
                        v -= dist;
                        break;

                    case "down":
                        v += dist;
                        break;

                    default:
                        System.err.println("unknown command: " + lineSplit[0]);
                        break;
                }
            }
            reader.close();
        } catch (Exception e) {
            System.out.println(e.getStackTrace());
        }

        System.out.println(h * v);
    }
}