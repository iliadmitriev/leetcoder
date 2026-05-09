#include <numeric>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int calPoints(vector<string> &operations) {
    vector<int> line;

    for (const auto &op : operations) {
      if (op == "C") {
        line.pop_back();
      } else if (op == "D") {
        line.push_back(line.back() * 2);
      } else if (op == "+") {
        line.push_back(line.back() + line[line.size() - 2]);
      } else {
        line.push_back(stoi(op));
      }
    }

    return std::accumulate(line.begin(), line.end(), 0);
  }
};