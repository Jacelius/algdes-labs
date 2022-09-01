package matching.data;

import java.util.*;

public class Person {
    private String name;
    private int id;
    private ArrayList<Integer> preferenceList;

    public Person(String name, int id) {
        this.name = name;
        this.id = id;
        this.preferenceList = new ArrayList<Integer>();
    }

    public String getName() {
        return this.name;
    }

    public void setPreferenceList(ArrayList<Integer> preferenceList) {
        this.preferenceList = preferenceList;
    }

    public ArrayList<Integer> getPreferenceList() {
        return this.preferenceList;
    }

    public int getId() {
        return this.id;
    }
}
