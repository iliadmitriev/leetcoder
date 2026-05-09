#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  const vector<string> digits = {
      "",        "One",     "Two",       "Three",    "Four",
      "Five",    "Six",     "Seven",     "Eight",    "Nine",
      "Ten",     "Eleven",  "Twelve",    "Thirteen", "Fourteen",
      "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
  };

  const vector<string> tens = {
      "",      "Ten",   "Twenty",  "Thirty", "Forty",
      "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
  };

  string helper(int num) {
    string v = "";

    if (num < 20) {
      v = digits[num];
    } else if (num < 100) {
      v = tens[num / 10] + " " + helper(num % 10);
    } else if (num < 1000) {
      v = digits[num / 100] + " Hundred " + helper(num % 100);
    } else if (num < 1000000) {
      v = helper(num / 1000) + " Thousand " + helper(num % 1000);
    } else if (num < 1000000000) {
      v = helper(num / 1000000) + " Million " + helper(num % 1000000);
    } else {
      v = helper(num / 1000000000) + " Billion " + helper(num % 1000000000);
    }

    if (v.size() && v.back() == ' ') {
      v.pop_back();
    }

    return v;
  }

public:
  string numberToWords(int num) {
    if (!num) {
      return "Zero";
    }

    return helper(num);
  }
};