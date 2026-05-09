class Solution {
public:
  bool isIsomorphic(string s, string t) {
    if (t.size() != s.size()) {
      return false;
    }

    unordered_map<char, char> d1, d2;
    for (int i = 0; i < s.size(); i++) {
      if (d1.find(s[i]) == d1.end() && d2.find(t[i]) == d2.end()) {
        d1[s[i]] = t[i];
        d2[t[i]] = s[i];
      } else if (d1[s[i]] != t[i] || d2[t[i]] != s[i]) {
        return false;
      }
    }

    return true;
  }
};