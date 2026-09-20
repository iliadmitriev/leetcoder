#include <ranges>
#include <string>

using std::string;

class Solution {
public:
    int reverseDegree(string s) {
        // const int base = 'a' + 26;
        // int v = 0;
        // for (int i = 0; i < s.size(); i++) {
        //     v += (i + 1) * (base - s[i]);
        // }
        // return v;

        const int base = 'a' + 26;

        auto v = s | std::views::enumerate |
                 std::views::transform([base](auto const& item) -> int {
                     auto const& [i, ch] = item;
                     return (i + 1) * (base - ch);
                 });

        return std::ranges::fold_left(v, 0, std::plus<int>());
    }
};