#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
  vector<string> findRepeatedDnaSequences(string s) {
    const int base = 7, length = 10;
    const int mod = int(1e9 + 7);

    if (s.size() < length) {
      return {};
    }

    vector<int> dict(100, 0);
    dict['A'] = 1, dict['C'] = 2, dict['G'] = 3, dict['T'] = 4;

    int prefix = 0, power = 1;
    for (int i = 0; i < length; i++) {
      prefix *= base;
      prefix += dict[s[i]];
      power *= base;
    }

    power /= base;
    int n = s.size();

    vector<string> result;
    unordered_map<int, int> seen({{prefix, 1}});

    for (int i = length; i < n; i++) {
      prefix -= dict[s[i - length]] * power;
      prefix *= base;
      prefix += dict[s[i]];

      if (seen[prefix] == 1) {
        result.push_back(s.substr(i - length + 1, length));
      }

      seen[prefix]++;
    }

    return result;
  }
};