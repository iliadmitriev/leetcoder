use std::collections::HashMap;

struct TrieNode {
  children: HashMap<char, TrieNode>,
  min_size: Option<usize>,
  index: Option<usize>,
}

impl TrieNode {
  fn new() -> Self {
    Self {
      children: HashMap::new(),
      min_size: None,
      index: None,
    }
  }

  fn update_if_shorter(&mut self, word_len: usize, new_index: usize) -> bool {
    if self.min_size.map_or(true, |s| word_len < s) {
      self.min_size = Some(word_len);
      self.index = Some(new_index);
      true
    } else {
      false
    }
  }
}

impl Default for TrieNode {
  fn default() -> Self {
    Self::new()
  }
}

pub struct Trie {
  root: TrieNode,
}


impl Trie {
  pub fn new() -> Self {
    Self {
      root: TrieNode::new(),
    }
  }

  pub fn insert(&mut self, word: &str, word_len: usize, new_index: usize) {
    let mut cur = &mut self.root;

    for ch in word.chars() {
      cur.update_if_shorter(word_len, new_index);

      cur = cur
        .children
        .entry(ch)
        .or_insert_with(TrieNode::new);
    }

    cur.update_if_shorter(word_len, new_index);
  }


  pub fn find(&self, word: &str) -> Option<usize> {
    let mut cur = &self.root;
    let mut result = self.root.index;

    for ch in word.chars() {
      match cur.children.get(&ch) {
        Some(node) => {
          cur = node;
          result = cur.index;
        },
        None => break,
      }
    }

    result
  }
}


impl Solution {
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        let n = words_container.len();
        let mut result: Vec<i32> = Vec::with_capacity(n);
        let mut trie = Trie::new();

        for (i, word) in words_container.iter().enumerate() {
          let rev: String = word.chars().rev().collect();
          trie.insert(rev.as_str(), rev.len(), i);
        }

        for word in words_query.iter() {
          let rev: String = word.chars().rev().collect();
          if let Some(idx) = trie.find(rev.as_str()) {
            result.push(idx as i32);
          }
        }

        result
    }
}