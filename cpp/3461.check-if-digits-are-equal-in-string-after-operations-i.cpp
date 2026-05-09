#include <deque>
#include <string>

using std::string, std::deque;

class Solution {
public:
  bool hasSameDigits(string s) {
    deque<int> q;

    for (char ch : s) {
      q.push_back(ch - '0');
    }

    while (q.size() > 2) {
      int prev = q.front();
      q.pop_front();
      int cnt = q.size();

      while (cnt--) {
        int cur = q.front();
        q.pop_front();

        q.push_back((cur + prev) % 10);
        prev = cur;
      }
    }

    return q.front() == q.back();
  }
};