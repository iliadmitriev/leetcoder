class Solution {
private:
    int gcd1(int a, int b) {
      int tmp;
      while (b) {
        tmp = b;
        b = a % b;
        a = tmp;
      }

      return a;
    }

    int gcd2(int a, int b) {
      while (a != b) {
        if (a > b) {
          a -= b;
        } else {
          b -= a;
        }
      }

      return a;
    }

public:
    int findGCD(vector<int>& nums) {
        int min_value = std::ranges::min(nums);
        int max_value = std::ranges::max(nums);

        return gcd2(max_value, min_value);
    }
};