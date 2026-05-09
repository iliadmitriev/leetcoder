class Solution {
private:
  vector<int> countRepeatingChars(string password) {
    vector<int> res;
    for (int i = 0; i < password.size(); i++) {
      if (i == 0 || password[i - 1] != password[i]) {
        res.push_back(1);
      } else {
        res.back()++;
      }
    }

    return res;
  }

  void breakWithDeletion(vector<int> &substringLengths, int deletions) {
    function<int(int)> key = [](int a) { return a >= 3 ? a % 3 : INT_MAX; };

    while (deletions > 0) {
      auto deletionIt =
          min_element(substringLengths.begin(), substringLengths.end(),
                      [&key](int a, int b) { return key(a) < key(b); });
      *deletionIt -= 1;
      deletions--;
    }
  }

public:
  int strongPasswordChecker(string password) {
    int missingTypes = 3;
    if (any_of(std::begin(password), std::end(password), ::isupper))
      missingTypes--;

    if (any_of(std::begin(password), std::end(password), ::islower))
      missingTypes--;

    if (any_of(std::begin(password), std::end(password), ::isdigit))
      missingTypes--;

    int deletions = max(0, (int)password.size() - 20);
    int insertions = max(0, 6 - (int)password.size());

    vector<int> substringLengths = countRepeatingChars(password);

    breakWithDeletion(substringLengths, deletions);

    int substringBreaks = 0;

    for (auto length : substringLengths) {
      if (length >= 3) {
        substringBreaks += length / 3;
      }
    }

    return deletions + max(insertions, max(missingTypes, substringBreaks));
  }
};