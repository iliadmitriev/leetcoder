#include <string>
#include <string_view>
#include <unordered_map>
#include <optional>
#include <memory>

class TrieNode {
  public:
    std::unordered_map<char, std::unique_ptr<TrieNode>> children;
    std::optional<size_t> min_size;
    std::optional<size_t> index;

    TrieNode() = default;

    void update_if_shorter(size_t word_len, size_t new_index) {
      if (!min_size || word_len < *min_size) {
        min_size = word_len;
        index = new_index;
      }
    }

    TrieNode& get_or_create(char ch, size_t word_len, size_t new_index) {
      auto& cur = children[ch];

      if (!cur) {
        cur = std::make_unique<TrieNode>();
      }

      cur->update_if_shorter(word_len, new_index);
      return *cur;
    }
};

class Trie {
  TrieNode root;

public:
  Trie() = default;

  template<std::ranges::range R>
  void insert(const R& word, size_t word_len, size_t new_index) {
    root.update_if_shorter(word_len, new_index);

    TrieNode* cur = &root;
    for (char ch : word) {
      cur = &cur->get_or_create(ch, word_len, new_index);
    }
  }

  template<std::ranges::range R>
  std::optional<size_t> find(const R& word) const {
    const TrieNode* cur = &root;
    std::optional<size_t> result = cur->index; // std::nullopt doesn't fit

    for (char ch : word) {
      auto it = cur->children.find(ch);

      if (it == cur->children.end()) {
        break;
      }

      cur = it->second.get();
      result = cur->index;
    }

    return result;
  }
};

class Solution {
public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        const auto n = wordsContainer.size();
        const auto m = wordsQuery.size();
        std::vector<int> result;
        result.reserve(m);

        auto trie = Trie();

        for (auto i = 0; i < n; i++) {
          auto rev = wordsContainer[i] | std::views::reverse;
          auto size = wordsContainer[i].size();

          trie.insert(rev, size, i);
        }

        for (auto i = 0; i < m; i++) {
          auto rev = wordsQuery[i] | std::views::reverse;
          auto res = trie.find(rev);

          if (res) {
            result.push_back(*res);
          }
        }

        return result;
    }
};