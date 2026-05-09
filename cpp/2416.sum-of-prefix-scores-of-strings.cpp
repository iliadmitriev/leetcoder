#include <algorithm>
#include <string>
#include <vector>
using std::string;
using std::vector;

const int N = 26;
const int SHIFT = 'a';

int static inline getKey(const char ch) { return ch - SHIFT; }

class TrieNode {
public:
  int count;
  TrieNode *children[N];

  TrieNode() : count(0), children{nullptr} {}
};

class Trie {
private:
  TrieNode *root;

public:
  Trie() : root(new TrieNode()) {}

  void addWord(const string &word) {
    TrieNode *node = root;

    for (char ch : word) {
      int key = getKey(ch);
      if (!node->children[key]) {
        node->children[key] = new TrieNode();
      }

      node = node->children[key];
      node->count++;
    }
  }

  void addWords(const vector<string> &words) {
    for (const string &word : words) {
      addWord(word);
    }
  }

  int getPrefixScore(const string &word) {
    int score = 0;
    TrieNode *node = root;

    for (char ch : word) {
      int key = getKey(ch);
      if (!node->children[key]) {
        break;
      }

      node = node->children[key];
      score += node->count;
    }
    return score;
  }
};

class Solution {
public:
  vector<int> sumPrefixScores(vector<string> &words) {
    vector<int> result(words.size());

    Trie trie = Trie();
    trie.addWords(words);

    std::transform(words.begin(), words.end(), result.begin(),
                   [&trie](const string &word) -> int {
                     return trie.getPrefixScore(word);
                   });

    return result;
  }
};
