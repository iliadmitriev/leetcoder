#include <sstream>
#include <string>

using namespace std;
class Solution {
public:
  int compareVersion(string version1, string version2) {
    istringstream v1(version1), v2(version2);
    string s1, s2;
    int d1, d2;

    while (!v1.eof() || !v2.eof()) {
      if (!v1.eof()) {
        getline(v1, s1, '.');
        d1 = stoi(s1);
      } else {
        d1 = 0;
      }

      if (!v2.eof()) {
        getline(v2, s2, '.');
        d2 = stoi(s2);
      } else {
        d2 = 0;
      }

      if (d1 == d2)
        continue;

      return d1 > d2 ? 1 : -1;
    }
    return 0;
  }
};