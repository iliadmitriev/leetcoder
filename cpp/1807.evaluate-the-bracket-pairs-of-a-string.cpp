#include <string>
#include <iostream>
#include <unordered_map>

using std::string;

class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
      const int n = s.size();

      std::stringstream res;
      std::unordered_map<string, string> voc;

      for (const auto& kv : knowledge) {
        voc[kv[0]] = kv[1];
      }

      for (int i = 0, j = 0; j <= n; j++) {
        if (j == n || s[j] == '(') {
          // terminal symbols outside the parentheses
          res << s.substr(i, j - i); 
          i = j + 1;
        } else if (s[j] == ')') {
          // key symbols inside the parentheses
          string key = s.substr(i, j - i);
          if (auto kv = voc.find(key); kv != voc.end()) {
            res << kv->second;
          } else {
            res << "?";
          }

          i = j + 1;
        }
      }
      
      return res.str();   
    }
};