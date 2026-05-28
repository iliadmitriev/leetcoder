import (
  "math"
  "slices"
)

type TrieNode struct {
  children map[byte]*TrieNode
  minSize int
  index int
}

func NewTrieNode() *TrieNode {
  return &TrieNode{
    children: make(map[byte]*TrieNode),
    minSize: math.MaxInt,
    index: -1,
  }
}

func (n *TrieNode) updateMin(size, index int) {
  if size < n.minSize {
    n.minSize = size
    n.index = index
  }
}


type Trie struct {
  root *TrieNode
}

func NewTrie() *Trie {
  return &Trie{
    root: NewTrieNode(),
  }
}

func (t *Trie) Insert(word []byte, size, index int) {
  node := t.root
  node.updateMin(size, index)

  for _, ch := range word {
    if _, exists := node.children[ch]; !exists {
      node.children[ch] = NewTrieNode()
    }

    node = node.children[ch]
    node.updateMin(size, index)
  }
}

func (t *Trie) Find(word []byte) int {
  node := t.root
  index := node.index

  for _, ch := range word {
    next, exists := node.children[ch]
    if !exists {
      break
    }

    node = next
    index = node.index
  }

  return index
}

func stringIndices(wordsContainer []string, wordsQuery []string) []int {
    result := make([]int, len(wordsQuery))
    trie := NewTrie();

    for i, word := range wordsContainer {
      rev := []byte(word)
      slices.Reverse(rev)

      trie.Insert(rev, len(word), i)
    }

    for i, word := range wordsQuery {
      rev := []byte(word)
      slices.Reverse(rev)

      result[i] = trie.Find(rev)
    }

    return result 
}