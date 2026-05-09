const LEN = 26

type PrefixTrieNode struct {
	count int
	child [LEN]*PrefixTrieNode
}

type PrefixTrie struct {
	root *PrefixTrieNode
}

func (p *PrefixTrieNode) SetChild(ch byte) *PrefixTrieNode {
	if p.child[ch] == nil {
		p.child[ch] = &PrefixTrieNode{}
	}

	return p.child[ch]
}

func (p *PrefixTrieNode) GetChild(ch byte) (*PrefixTrieNode, bool) {
	if p.child[ch] == nil {
		return nil, false
	}

	return p.child[ch], true
}

func (p *PrefixTrieNode) Inc() {
	p.count++
}

func (p *PrefixTrieNode) GetCount() int {
	return p.count
}

func NewPrefixTrie() PrefixTrie {
	return PrefixTrie{root: &PrefixTrieNode{}}
}

func (t *PrefixTrie) AddWord(word string) {
	node := t.root
	for i := 0; i < len(word); i++ {
		node = node.SetChild(word[i] - 'a')
		node.Inc()
	}
}

func (t *PrefixTrie) AddListWords(words []string) {
	for i := range words {
		t.AddWord(words[i])
	}
}

func (t *PrefixTrie) GetPrefixScore(word string) int {
	score := 0
	node := t.root
	for i := 0; i < len(word); i++ {
		if nextNode, ok := node.GetChild(word[i] - 'a'); ok {
			node = nextNode
			score += node.GetCount()
		} else {
			break
		}
	}

	return score
}

func sumPrefixScores(words []string) []int {
	result := make([]int, len(words))

	trie := NewPrefixTrie()
	trie.AddListWords(words)

	for i := range words {
		result[i] = trie.GetPrefixScore(words[i])
	}

	return result
}
