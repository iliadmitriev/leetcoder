class Solution {
private:
  bool checkWordFit(const string &word, const vector<int> &letterMap,
                    const vector<int> &scoreMap) {
    vector<int> wordMap(26, 0);
    for (char c : word) {
      wordMap[c - 97]++;
    }

    for (int i = 0; i < 26; i++) {
      if (letterMap[i] < wordMap[i]) {
        return false;
      }
    }

    return true;
  }

  int countWordScore(const string &word, const vector<int> &scoreMap,
                     vector<int> &letterMap) {
    int score = 0;
    for (char c : word) {
      score += scoreMap.at(c - 97);
      letterMap[c - 97]--;
    }
    return score;
  }

  void returnWordLetters(const string &word, vector<int> &letterMap) {
    for (char c : word) {
      letterMap[c - 97]++;
    }
  }

  int dfsFindMaxWordsScore(vector<int> &letterMap, const vector<string> &words,
                           const vector<int> scoreMap, int i, int score) {
    if (i == words.size()) {
      return score;
    }

    int res = dfsFindMaxWordsScore(letterMap, words, scoreMap, i + 1, score);
    if (checkWordFit(words[i], letterMap, scoreMap)) {
      int currScore = countWordScore(words[i], scoreMap, letterMap);
      res = max(res, dfsFindMaxWordsScore(letterMap, words, scoreMap, i + 1,
                                          score + currScore));
      returnWordLetters(words[i], letterMap);
    }

    return res;
  }

public:
  int maxScoreWords(vector<string> &words, vector<char> &letters,
                    vector<int> &score) {
    vector<int> letterMap(26, 0);

    for (char c : letters) {
      letterMap[c - 97]++;
    }

    return dfsFindMaxWordsScore(letterMap, words, score, 0, 0);
  }
};