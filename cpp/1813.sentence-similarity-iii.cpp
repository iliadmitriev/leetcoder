#include <deque>
#include <sstream>
#include <string>

using std::deque, std::string;

class Solution {
private:
  // splits input string by delimiter and puts into deque
  // returns number of tokens
  int split(const string &s, deque<string> &deq, char delimiter = ' ') {
    int counter = 0;
    std::stringstream ss(s);

    for (string token; std::getline(ss, token, delimiter); counter++) {
      deq.push_back(token);
    }

    return counter;
  }

public:
  bool areSentencesSimilar(string sentence1, string sentence2) {
    deque<string> q1, q2;
    int len1 = split(sentence1, q1);
    int len2 = split(sentence2, q2);

    if (len1 > len2) {
      std::swap(q1, q2);
    }

    while (q1.size() && q1.front() == q2.front()) {
      q1.pop_front();
      q2.pop_front();
    }

    while (q1.size() && q1.back() == q2.back()) {
      q1.pop_back();
      q2.pop_back();
    }

    return !q1.size();
  }
};