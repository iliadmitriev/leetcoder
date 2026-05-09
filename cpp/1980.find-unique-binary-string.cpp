#include <bitset>
#include <string>
#include <unordered_set>
#include <vector>

using std::string, std::unordered_set, std::vector;

class Solution {
public:
  string findDifferentBinaryString(vector<string> &nums) {
    unordered_set<int> seen;
    const int n = nums.back().size();
    const int N = 1 << n;

    for (const string &num : nums) {
      seen.insert(std::stoi(num, 0, 2));
    }

    for (int v = 0; v < N; v++) {
      if (!seen.count(v)) {
        return std::bitset<16>(v).to_string().substr(16 - n);
      }
    }

    return "";
  }
};