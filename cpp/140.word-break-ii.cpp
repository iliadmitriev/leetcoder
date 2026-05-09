class Solution {
private:
  void dfs(const set<string> &words, const string &s, int i,
           vector<string> &path, vector<vector<string>> &res) {
    if (i == s.size()) {
      res.push_back(path);
      return;
    }

    for (int j = i + 1; j <= s.size(); j++) {
      string word = s.substr(i, j - i);
      if (words.count(word)) {
        path.push_back(word);
        dfs(words, s, j, path, res);
        path.pop_back();
      }
    }
  }

  static string joinSpace(const vector<string> &words) {
    if (!words.size())
      return "";

    stringstream res;
    res << words[0];

    for (int i = 1; i < words.size(); i++) {
      res << " " << words[i];
    }

    return res.str();
  }

public:
  vector<string> wordBreak(string s, vector<string> &wordDict) {
    set<string> words(wordDict.begin(), wordDict.end());
    vector<vector<string>> res;
    vector<string> path;
    dfs(words, s, 0, path, res);

    vector<string> ret;
    transform(res.begin(), res.end(), back_inserter(ret), joinSpace);
    return ret;
  }
};