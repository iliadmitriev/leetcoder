#include <string>

using namespace std;

class Solution {
public:
  string reversePrefix(string word, char ch) {
    size_t pos = word.find_first_of(ch);
    string rev = word.substr(0, pos + 1);
    return pos == string::npos
               ? word
               : string(rev.rbegin(), rev.rend()) + word.substr(pos + 1);
  }
};