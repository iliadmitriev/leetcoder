class Solution {
  public int furthestDistanceFromOrigin(String moves) {
    int spc = 0, pos = 0;

    for (char move : moves.toCharArray()) {
      switch (move) {
        case 'L':
          pos--;
          break;
        case 'R':
          pos++;
          break;
        case '_':
          spc++;
          break;
      }
    }

    return Math.abs(pos) + spc;
  }
}