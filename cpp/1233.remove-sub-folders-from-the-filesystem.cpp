#include <string>
#include <vector>

using std::vector, std::string;

class Solution {
public:
  vector<string> removeSubfolders(vector<string> &folder) {

    vector<string> res;

    std::sort(folder.begin(), folder.end());

    for (string f : folder) {
      if (res.empty() ||
          f.substr(0, res.back().size() + 1) != res.back() + '/') {
        res.push_back(f);
      }
    }

    return res;
  }
};