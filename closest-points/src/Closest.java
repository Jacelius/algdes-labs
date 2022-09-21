import java.util.ArrayList;
import java.util.Scanner;

public class Closest {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Coord> coords = new ArrayList<>();

        // parsing input
        String s = sc.nextLine();
        while (!s.contains("NODE_COORD_SECTION")) {
            s = sc.nextLine();
        }

        while (sc.hasNextInt()) {
            sc.nextInt(); // skip the first number for id
            int x = sc.nextInt();
            int y = sc.nextInt();

            coords.add(new Coord(x, y));
        }

        sc.close();

        // Divide & Conquer algorithm: find the closest pair
        // sort coords by x axis
        coords.sort((c1, c2) -> c1.x - c2.x);

        DivideAndConquerClosestPairs(coords, getMedian(coords));
    }

    public static double getMedian(ArrayList<Coord> coords) {
        int size = coords.size();
        if (size % 2 == 0) {
            return (coords.get(size / 2).x + coords.get(size / 2 - 1).x) / 2.0;
        } else {
            return coords.get(size / 2).x;
        }

    }

    public static void DivideAndConquerClosestPairs(ArrayList<Coord> coords, double median) {
        // Given a sorted arraylist of Coords print the pair with the minimum distance
        if (coords.size() < 3) {

        }

        // Split coords into two sublists split by median
        // Sublist has O(1) time complexity
        if (coords.size() % 2 == 0) {
            ArrayList<Coord> left = (ArrayList<Closest.Coord>) coords.subList(0, coords.size() / 2);
            ArrayList<Coord> right = (ArrayList<Closest.Coord>) coords.subList(coords.size() / 2 + 1, coords.size());
        } else {
            int medianIndex = (int) (Math.floor(coords.size() / 2));
            ArrayList<Coord> left = (ArrayList<Closest.Coord>) coords.subList(0, medianIndex);
            ArrayList<Coord> right = (ArrayList<Closest.Coord>) coords.subList(medianIndex + 1 / 2 + 1, coords.size());
        }

        // Output should be {filename} {dimension} {closets pair distance}

    }

    public static class Coord {
        int x;
        int y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return this.x + " " + this.y;
        }
    }

}