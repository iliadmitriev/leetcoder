
func stringMatching(words []string) []string {
	trie := NewTrie()

	res := make([]string, 0)

	for _, word := range words {
		for i := 0; i < len(word); i++ {
			trie.AddWord(word[i:])
		}
	}

	for _, word := range words {
		if trie.IsSubstr(word) {
			res = append(res, word)
		}
	}

	return res
}

type TrieNode struct {
	Child [26]*TrieNode
	Count int
}

type Trie struct {
	root *TrieNode
}

func NewTrie() Trie {
	return Trie{root: &TrieNode{}}
}

func (t *Trie) AddWord(word string) {
	node := t.root

	for i := 0; len(word) > i; i++ {
		if node.Child[word[i]-'a'] == nil {
			node.Child[word[i]-'a'] = &TrieNode{}
		}

		node = node.Child[word[i]-'a']
		node.Count++
	}
}

func (t *Trie) IsSubstr(word string) bool {
	node := t.root

	for i := 0; len(word) > i; i++ {
		if node.Child[word[i]-'a'] == nil {
			return false
		}
		node = node.Child[word[i]-'a']
	}

	return node.Count > 1
}
