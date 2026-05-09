#include <array>
#include <deque>
#include <string>

using std::array, std::string, std::deque;

class Solution {
public:
  string sortString(string s) {
    const int base = 'a';
    string res;

    array<int, 26> cnt = {0};
    for (char ch : s) {
      cnt[ch - base]++;
    }

    deque<int> q;
    for (int i = 0; i < 26; i++) {
      if (cnt[i]) {
        q.push_back(i);
      }
    }

    while (q.size()) {
      for (int k = q.size(); k > 0; k--) {
        int i = q.front();
        q.pop_front();
        res.push_back(base + i);
        cnt[i]--;

        if (cnt[i]) {
          q.push_back(i);
        }
      }

      for (int k = q.size(); k > 0; k--) {
        int i = q.back();
        q.pop_back();
        res.push_back(base + i);
        cnt[i]--;

        if (cnt[i]) {
          q.push_front(i);
        }
      }
    }

    return res;
  }
};