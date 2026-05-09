#include <string>
#include <vector>
using std::vector, std::string;

class Solution {
public:
  vector<int> partitionLabels(string s) {
    vector<int> res;
    vector<int> last(26, 0);
    int end = 0, j = 0;

    for (int i = 0; i < s.size(); i++) {
      last[s[i] - 'a'] = i;
    }

    for (int i = 0; i < s.size(); i++) {
      end = std::max(end, last[s[i] - 'a']);
      if (i == end) {
        res.push_back(end - j + 1);
        j = end + 1;
      }
    }

    return res;
  }
};