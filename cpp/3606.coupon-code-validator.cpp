#include <algorithm>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using std::vector, std::string, std::unordered_set, std::pair;

class Solution {
public:
  vector<string> validateCoupons(vector<string> &code,
                                 vector<string> &businessLine,
                                 vector<bool> &isActive) {
    const size_t n = code.size();
    const unordered_set<string> validBusinessLines = {"electronics", "grocery",
                                                      "pharmacy", "restaurant"};

    vector<pair<string, string>> filtered;

    auto isValidCodeId = [](const string &codeId) {
      // check if codeId consits only from [A-Za-z0-9_]
      for (const char c : codeId) {
        if (!isalnum(c) && c != '_') {
          return false;
        }
      }

      return true;
    };

    for (int i = 0; i < n; i++) {
      if (!isActive[i]) {
        continue;
      }

      const string &business = businessLine[i];
      if (validBusinessLines.find(business) == validBusinessLines.end()) {
        continue;
      }

      const string &codeId = code[i];
      if (codeId.size() == 0) {
        continue;
      }

      if (!isValidCodeId(codeId)) {
        continue;
      }

      filtered.emplace_back(business, codeId);
    }

    std::sort(filtered.begin(), filtered.end());

    vector<string> result;
    for (const auto &[_, codeId] : filtered) {
      result.push_back(codeId);
    }

    return result;
  }
};