#include <algorithm>
#include <string>
#include <vector>

using std::string;
using std::vector;

const int ALPHA = 26;
class TrieNode {
public:
  TrieNode *child[ALPHA];
};

class Trie {
private:
  TrieNode *_root;

public:
  Trie() : _root(nullptr) {}

  void addWord(const string &word) {
    if (!_root) {
      _root = new TrieNode();
    }

    auto node = _root;
    for (char ch : word) {
      if (!node->child[ch - 'a'])
        node->child[ch - 'a'] = new TrieNode();
      node = node->child[ch - 'a'];
    }
  }

  bool isSubstr(const string &word) {
    if (!_root) {
      return false;
    }

    auto node = _root;
    for (char ch : word) {
      if (!node->child[ch - 'a'])
        return false;
      node = node->child[ch - 'a'];
    }

    return true;
  }
};

class Solution {
public:
  vector<string> stringMatching(vector<string> &words) {

    std::sort(words.begin(), words.end(),
              [](string &a, string &b) -> bool { return a.size() > b.size(); });

    vector<string> res;
    Trie trie;

    for (string &word : words) {
      if (trie.isSubstr(word)) {
        res.push_back(word);
      }

      // add all possible substrings
      for (int i = 0; i < word.size(); i++) {
        trie.addWord(word.substr(i));
      }
    }

    return res;
  }
};