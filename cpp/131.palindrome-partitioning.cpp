
class Solution {
private:
  void dfs(vector<vector<string>> &res, vector<string> &path, string &s,
           int i) {
    if (i >= s.size()) {
      res.push_back(path);
    }

    for (int j = i + 1; j < s.size() + 1; j++) {
      if (isPal(s, i, j - 1)) {
        path.push_back(s.substr(i, j - i));
        dfs(res, path, s, j);
        path.pop_back();
      }
    }
  }

  bool isPal(string &s, int i, int j) {

    while (i < j) {
      if (s[i] != s[j]) {
        return false;
      }

      i++;
      j--;
    }

    return true;
  }

public:
  vector<vector<string>> partition(string s) {
    vector<vector<string>> res;
    vector<string> path;
    dfs(res, path, s, 0);
    return res;
  }
};