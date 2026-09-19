func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
    dist := func(ax, ay, bx, by int) int {
      dx := ax - bx
      dy := ay - by

      return dx * dx + dy * dy
    }

    // calculate the coordinates of the point inside the rectangle closest to the circle center
    x := max(x1, min(x2, xCenter)) 
    y := max(y1, min(y2, yCenter))

    // if x, y is inside the circle
    return dist(x, y, xCenter, yCenter) <= radius * radius
}