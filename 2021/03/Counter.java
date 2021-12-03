import java.util.HashMap;
import java.util.Map;

// https://stackoverflow.com/questions/32348453/python-counter-alternative-for-java
public class Counter<T> {
    final Map<T, Integer> counts = new HashMap<>();

    public void add(T t) {
        counts.merge(t, 1, Integer::sum);
    }

    public int count(T t) {
        return counts.getOrDefault(t, 0);
    }
}