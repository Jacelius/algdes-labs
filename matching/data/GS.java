package matching.data;

import java.util.*;

class GS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        int n = Integer.parseInt(s.substring(2, s.length()));
        ArrayList<Person> rejecters = new ArrayList<Person>();
        ArrayList<Person> proposers = new ArrayList<Person>();
        ArrayList<Person> TotalPersonList = new ArrayList<Person>();

        for (int i = 1; i <= 2 * n; i++) {
            int id = sc.nextInt();
            String name = sc.next();

            if (i % 2 == 1) { // male
                proposers.add(new Person(name, id));
            } else { // female
                rejecters.add(new Person(name, id));
            }
        }
        TotalPersonList.addAll(proposers);
        TotalPersonList.addAll(rejecters);

        String throwaway = sc.nextLine();
        String throwaway2 = sc.nextLine();

        // Fill preference lists
        for (int i = 1; i <= 2 * n; i++) {
            String newline = sc.nextLine();
            String[] SplitonColon = newline.split(":");
            System.out.println(SplitonColon.toString());
            int personid = Integer.parseInt(SplitonColon[0]);
            Person p = getPersonById(personid, TotalPersonList);
            String[] preferences = SplitonColon[1].split(" ");
            String[] modifiedprefernces = Arrays.copyOfRange(preferences, 1, preferences.length);
            ArrayList<Integer> idprefs = new ArrayList<Integer>();
            for (String str : modifiedprefernces) {
                idprefs.add(Integer.parseInt(str));
            }
            p.setPreferenceList(idprefs);
        }
        System.out.println((proposers.get(0).getPreferenceList()));
        sc.close();

    }

    public static Person getPersonById(int id, ArrayList<Person> totalList) {
        for (Person p : totalList) {
            if (p.getId() == id) {
                return p;
            }
        }
        return null;
    }

    public static class Person {
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

}
