#include <string>
using std::string;

class Solution {
public:
  string decodeCiphertext(string encodedText, int rows) {
    const int n = encodedText.size();
    const int cols = n / rows;

    if (rows == 1) {
      return encodedText;
    }

    string res;

    for (int start = 0; start < cols; start++) {
      for (int i = 0, j = start; i < rows && j < cols; i++, j++) {
        res.push_back(encodedText[i * cols + j]);
      }
    }

    while (res.size() && res.back() == ' ') {
      res.pop_back();
    }

    return res;
  }
};