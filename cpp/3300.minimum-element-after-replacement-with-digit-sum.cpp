class Solution {
public:
    int minElement(vector<int>& nums) {
        auto digit = [](int x) -> int {
          int sum = 0;
          while (x > 0) {
            sum += x % 10;
            x /= 10;
          }

          return sum;
        };

        auto value = nums | std::views::transform(digit);
        return std::ranges::min(value);
    }
};