#include <sstream>
#include <string>
using std::string;

class Solution {
private:
  bool isVowel(char c) {
    char ch = std::tolower(c);
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
  }

public:
  string toGoatLatin(string sentence) {
    const int n = sentence.size();
    std::stringstream ss;
    string extra = "ma";

    for (int i = 0, j = 0; i < n; i = j + 1) {
      j = i;
      while (j < n && sentence[j] != ' ') {
        j++;
      }

      extra += "a";
      string word = sentence.substr(i, j - i);
      ss << (isVowel(word[0]) ? word : word.substr(1) + word[0]) << extra;

      if (j < n) {
        ss << " ";
      }
    }

    return ss.str();
  }
};