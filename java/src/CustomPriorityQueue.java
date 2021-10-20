import java.util.*;

public class CustomPriorityQueue{
    public static void main(String[] args){

        PriorityQueue<Entry> priorityQueue = new PriorityQueue<Entry>();

        priorityQueue.add(new Entry(Integer.valueOf(1), new ArrayList<>(Arrays.asList(0, 5))));
        priorityQueue.add(new Entry(Integer.valueOf(2), new ArrayList<>(Arrays.asList(2, 3))));
        priorityQueue.add(new Entry(Integer.valueOf(3), new ArrayList<>(Arrays.asList(4, 4))));
        priorityQueue.add(new Entry(Integer.valueOf(4), new ArrayList<>(Arrays.asList(5, 2))));
        priorityQueue.add(new Entry(Integer.valueOf(5), new ArrayList<>(Arrays.asList(7, 1))));

        System.out.println(priorityQueue);

        while (priorityQueue.size() != 0){
            System.out.println(priorityQueue.poll().toString());
        }

    }

}

class Entry implements Comparable<Entry> {

    private Integer key;
    private ArrayList value;

    public Entry(Integer key, ArrayList value) {
        this.key = key;
        this.value = value;
    }

    public Integer getKey() {
        return key;
    }

    public void setKey(Integer key) {
        this.key = key;
    }

    public ArrayList getValue() {
        return value;
    }

    public void setValue(ArrayList value) {
        this.value = value;
    }

    @Override
    public int compareTo(Entry o) {

        if ((int) this.value.get(1) > (int) o.value.get(1)){
            return 1;
        }
        if ((int)this.value.get(1) < (int) o.value.get(1)){
            return -1;
        }
        return 0;

    }

    @Override
    public String toString() {
        return "key ::: " + key + " value ::: " + value;
    }
}



