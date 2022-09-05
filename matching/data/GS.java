package matching.data;

import java.util.*;

class GS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // parsing input
        String s = sc.nextLine();
        while (s.contains("#"))
            s = sc.nextLine();

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

        sc.nextLine();
        sc.nextLine();

        // Fill preference lists
        for (int i = 1; i <= 2 * n; i++) {
            String newline = sc.nextLine();
            String[] SplitonColon = newline.split(":");
            int personid = Integer.parseInt(SplitonColon[0]);
            Person p = getPersonById(personid, TotalPersonList);
            String[] preferences = SplitonColon[1].split(" ");
            String[] modifiedpreferences = Arrays.copyOfRange(preferences, 1, preferences.length);
            ArrayList<Integer> idprefs = new ArrayList<Integer>();
            for (String str : modifiedpreferences) {
                idprefs.add(Integer.parseInt(str));
            }
            p.setPreferenceList(idprefs);
        }

        // Gale-Shapley algorithm
        ArrayList<Person> freeProposers = new ArrayList<>(proposers);
        while (freeProposers.size() > 0) {
            Person man = freeProposers.get(0);
            // get man's highest ranked woman, who he hasn't been proposed to
            Integer womanId = man.getPreferenceList().get(0);
            Person woman = getPersonById(womanId, rejecters);
            if (!woman.isEngaged) { // get engaged
                man.setIsEngaged(true);
                woman.setIsEngaged(true);
                woman.setEngagedToId(man.id);
                man.setEngagedToId(womanId);
                man.getPreferenceList().remove(0); // "cross off" woman in pref list
                freeProposers.remove(0); // remove man from freeProposers
            } else {
                // woman is engaged, so she will compare man to her current man
                ArrayList<Integer> womanPrefList = woman.getPreferenceList();
                int currentManId = woman.engagedToId;

                // if current man id is earlier in womanPrefList, get engaged
                if (AisBeforeB(man.id, currentManId, womanPrefList)) { // get engaged
                    Person currentMan = getPersonById(currentManId, TotalPersonList);
                    currentMan.setIsEngaged(false);
                    freeProposers.add(currentMan); // yeet current man back to freeProposers
                    freeProposers.remove(0); // remove new man
                    man.setEngagedToId(womanId);
                    woman.setEngagedToId(man.id);

                } else { // stay engaged
                    man.getPreferenceList().remove(0); // "cross off" woman in pref list
                }
            }
        }
        for (Person p : proposers) {
            System.out.println(p.name + " -- " + getPersonById(p.engagedToId, TotalPersonList).name);
        }
        sc.close();
    }

    public static boolean AisBeforeB(int a, int b, ArrayList<Integer> list) {
        int indexA = list.indexOf(a);
        int indexB = list.indexOf(b);
        if (indexA < indexB)
            return true;
        else
            return false;
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
        private boolean isEngaged;
        private int engagedToId;

        public Person(String name, int id) {
            this.name = name;
            this.id = id;
            this.preferenceList = new ArrayList<Integer>();
            this.isEngaged = false;
        }

        public String getName() {
            return this.name;
        }

        public boolean getIsEngaged() {
            return this.isEngaged;
        }

        public void setIsEngaged(boolean b) {
            this.isEngaged = b;
        }

        public void setEngagedToId(int id) {
            this.engagedToId = id;
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
