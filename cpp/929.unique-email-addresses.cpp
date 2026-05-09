#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using std::string;
using std::unordered_set;
using std::vector;

class Solution {
private:
  string unify(string email) {
    int i = 0, n = email.size();
    std::stringstream ss;

    while (i < n && email[i] != '+' && email[i] != '@') {
      if (email[i] == '.') {
        i++;
        continue;
      }

      ss << email[i++];
    }

    while (i < n && email[i] != '@') {
      i++;
    }

    ss << email.substr(i, n - i);

    return ss.str();
  }

public:
  int numUniqueEmails(vector<string> &emails) {

    unordered_set<string> seen;
    for (auto email : emails) {
      seen.insert(unify(email));
    }

    return seen.size();
  }
};