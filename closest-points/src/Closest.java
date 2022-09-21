import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.awt.geom.Point2D;

public class Closest {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Coord> coords = new ArrayList<>();

        // parsing input
        String s = sc.nextLine();
        while (!s.contains("NODE_COORD_SECTION")) {
            s = sc.nextLine();
        }

        int numpoints = 0;

        while (sc.hasNextInt()) {
            numpoints = sc.nextInt(); // skip the first number for id

            double x = Double.valueOf(sc.next());
            double y = Double.valueOf(sc.next());

            coords.add(new Coord(x, y));
        }

        sc.close();

        // Divide & Conquer algorithm: find the closest pair
        // sort coords by x axis
        coords.sort((c1, c2) -> (int) c1.x - (int) c2.x);
        System.out.println(numpoints + " " + DivideAndConquerClosestPairs(coords));
    }

    public static double ClosestPointsBrute(List<Coord> coords) {
        double min = Double.MAX_VALUE;
        for (int i = 0; i < coords.size(); i++) {
            for (int j = i + 1; j < coords.size(); j++) {
                min = Math.min(min, Coord.getDistance(coords.get(i), coords.get(j)));
            }
        }

        return min;
    }

    public static double DivideAndConquerClosestPairs(List<Coord> coords) {
        // Given a sorted arraylist of Coords print the pair with the minimum distance
        if (coords.size() <= 3) {
            return ClosestPointsBrute(coords);
        }
        List<Coord> left = new ArrayList<Coord>();
        List<Coord> right = new ArrayList<Coord>();

        // Split coords into two about equally sized sublists
        // Sublist has O(1) time complexity
        if (coords.size() % 2 == 0) {
            left = coords.subList(0, coords.size() / 2);
            right = coords.subList(coords.size() / 2 + 1, coords.size());
        } else {
            int medianIndex = (int) (Math.floor(coords.size() / 2));
            left = coords.subList(0, medianIndex);
            right = coords.subList(medianIndex + 1 / 2 + 1, coords.size());
        }

        double min = Math.min(DivideAndConquerClosestPairs(left), DivideAndConquerClosestPairs(right));

        // Output should be {filename} {dimension} {closets pair distance}

        return min; // Change this when we have a resultx
    }

    public static class Coord {
        double x;
        double y;

        public Coord(double x, double y) {
            this.x = x;
            this.y = y;
        }

        // Function to get distance between coords
        public static double getDistance(Coord a, Coord b) {
            return Point2D.distance(a.x, a.y, b.x, b.y);
        }

        @Override
        public String toString() {
            return this.x + " " + this.y;
        }
    }

}