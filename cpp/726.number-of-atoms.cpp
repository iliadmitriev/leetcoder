#include <algorithm>
#include <cctype>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using std::function;
using std::pair;
using std::sort;
using std::string;
using std::stringstream;
using std::unordered_map;
using std::vector;

typedef unordered_map<string, int> atom_map;
typedef vector<atom_map> stack_map;

class Solution {
private:
  void tokenize(string &s, function<void(string)> f) {
    int i = 0;
    while (i < s.size()) {

      if (s[i] == '(') {
        f(s.substr(i, 1));
        i++;
      } else if (s[i] == ')') {
        f(s.substr(i, 1));
        i++;
      } else if (std::isdigit(s[i])) {
        int j = 1;
        while (i + j < s.size() && std::isdigit(s[i + j]))
          j++;
        f(s.substr(i, j));
        i += j;
      } else if (std::isalpha(s[i])) {
        int j = 1;
        while (i + j < s.size() && std::isalpha(s[i + j]) &&
               std::islower(s[i + j]))
          j++;
        f(s.substr(i, j));
        i += j;
      } else {
        i++;
      }
    }
  }

  atom_map flatten(stack_map &st) {
    atom_map res;
    while (st.size() && st.back().size()) {
      for (auto &[k, v] : st.back()) {
        res[k] += v;
      }
      st.pop_back();
    }
    if (st.size() && !st.back().size()) {
      st.pop_back();
    }
    return res;
  }

  void pprint(stack_map &st) {
    for (auto &el : st) {
      for (auto &[k, v] : el) {
        std::cout << k << " " << v << ", ";
      }
      std::cout << " * ";
    }
    std::cout << std::endl;
  }

public:
  string countOfAtoms(string formula) {

    stack_map st;
    st.push_back({});

    tokenize(formula, [&](string tok) {
      if (tok == "(") {
        st.push_back({});
      } else if (tok == ")") {
        atom_map cur = flatten(st);
        st.push_back(cur);
      } else if (std::isdigit(tok[0])) {
        int cnt = stoi(tok);
        for (auto &[_, v] : st.back()) {
          v *= cnt;
        }
      } else if (std::isalpha(tok[0])) {
        st.push_back({{tok, 1}});
      }
    });

    atom_map res = flatten(st);
    vector<pair<string, int>> sorted(res.begin(), res.end());
    sort(sorted.begin(), sorted.end(),
         [](const pair<string, int> &a, const pair<string, int> &b) {
           return a.first < b.first;
         });

    stringstream ss;
    for (auto &[k, v] : sorted) {
      ss << k;
      if (v > 1)
        ss << v;
    }

    return ss.str();
  }
};