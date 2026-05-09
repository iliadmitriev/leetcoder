#include <cstdlib>
#include <string>
#include <unordered_map>
using std::string, std::unordered_map;

class Solution {
public:
  string fractionToDecimal(int numerator, int denominator) {
    if (!numerator) {
      return "0";
    }

    string res;
    if (numerator < 0 ^ denominator < 0) {
      res.push_back('-');
    }

    unsigned long num = std::abs(long(numerator));
    unsigned long den = std::abs(long(denominator));

    res += std::to_string(num / den);
    num %= den;
    num *= 10;

    if (!num) {
      return res;
    }

    res.push_back('.');
    unordered_map<int, int> cache;

    while (num && cache.find(num) == cache.end()) {
      cache[num] = res.size();
      res += std::to_string(num / den);
      num %= den;
      num *= 10;
    }

    if (num) {
      res.insert(cache[num], "(");
      res.push_back(')');
    }

    return res;
  }
};