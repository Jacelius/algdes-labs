import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.awt.geom.Point2D;
import java.text.DecimalFormat;

public class Closest {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Coord> coords = new ArrayList<>();

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
        coords.sort((Coord c1, Coord c2) -> Double.compare(c1.x, c2.x));
        double closest = DivideAndConquerClosestPairs(coords);

        DecimalFormat df = new DecimalFormat("###.##############");
        String formatted = df.format(closest);
        System.out.println(numpoints + " " + formatted);
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

        int median = coords.size() / 2;
        // Sublist has O(1) time complexity
        left = coords.subList(0, median);
        right = coords.subList(median, coords.size());

        double min = Math.min(DivideAndConquerClosestPairs(left), DivideAndConquerClosestPairs(right));

        List<Coord> bl = new ArrayList<>();
        List<Coord> br = new ArrayList<>();
        for (Coord coord : left) {
            if (coord.x >= (coords.get(median).x - min)) {
                bl.add(coord);
            }
        }
        for (Coord coord : right) {
            if (coord.x <= (coords.get(median).x + min)) {
                br.add(coord);
            }
        }

        // sort br by y axis
        br.sort((Coord c1, Coord c2) -> Double.compare(c1.y, c2.y));

        // search for highest point in br min * 2min box
        for (Coord coord : bl) {
            for (int i = 0; i < br.size(); i++) {
                if (br.get(i).y >= (coord.y - min) && br.get(i).y <= (coord.y + min)) {
                    min = Math.min(min, Coord.getDistance(coord, br.get(i)));
                }
            }
        }

        return min;
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