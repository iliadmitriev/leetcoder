#include <vector>

using std::vector;

class Solution {
public:
  vector<int> decode(vector<int> &encoded, int first) {
    vector<int> decoded;
    int n = encoded.size();

    decoded.reserve(n);
    decoded.push_back(first);

    for (int i = 0; i < n; i++) {
      decoded.push_back(encoded[i] ^ decoded[i]);
    }

    return decoded;
  }
};