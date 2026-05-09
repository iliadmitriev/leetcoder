
class Solution {
    // Java 16+ tuple
    public class Point {
      private int x, y;

      public Point(int x, int y) {
        this.x = x;
        this.y = y;
      }

      public void inc(int dx, int dy) {
        x += dx;
        y += dy;
      }

      public void dec(int dx, int dy) {
        x -= dx;
        y -= dy;
      }

      public int getDist() {
          return x * x + y * y;
      }

      @Override
      public boolean equals(Object other) {
        if (!(other instanceof Point point)) {
          return false;
        }
        return x == point.x && y == point.y;
      }

      @Override
      public int hashCode() {
        return x * 31 + y;
      }
    }

    public Set<Point> toCoordinateSet(int[][] points) {
        if (points == null) return new HashSet<>();

        return Arrays.stream(points)
          .filter(arr -> arr != null && arr.length == 2) // just for safety
          .map(point -> new Point(point[0], point[1]))
          .collect(Collectors.toCollection(HashSet::new));
    }

    public int robotSim(int[] commands, int[][] obstacles) {
        int dx = 0, dy = 1; // staring direction delta: facing north
        int farest = 0; // return value

        Set<Point> obstaclesSet = toCoordinateSet(obstacles);
        Point pos = new Point(0, 0);

        for (int cmd : commands) {
          switch (cmd) {
            case -1 -> { // clockwise
              int tmpDX = dx;
              dx = dy;
              dy = -tmpDX;
            }
            case -2 -> { // counterclockwise
              int tmpDX = dx;
              dx = -dy;
              dy = tmpDX;
            }
            default -> {
              while (cmd-- > 0) {
                  pos.inc(dx, dy);

                  if (obstaclesSet.contains(pos)) {
                    pos.dec(dx, dy);
                    break;
                  }
              }
            }
          }

          farest = Math.max(farest, pos.getDist());
        }

        return farest;
    }
}