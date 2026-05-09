import (
	"container/list"
	"strings"
)

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	l1, l2 := list.New(), list.New()

	for _, word := range strings.Split(sentence1, " ") {
		l1.PushBack(word)
	}

	for _, word := range strings.Split(sentence2, " ") {
		l2.PushBack(word)
	}

	if l1.Len() > l2.Len() {
		l2, l1 = l1, l2
	}

	for l1.Len() > 0 && l1.Front().Value == l2.Front().Value {
		l1.Remove(l1.Front())
		l2.Remove(l2.Front())
	}

	for l1.Len() > 0 && l1.Back().Value == l2.Back().Value {
		l1.Remove(l1.Back())
		l2.Remove(l2.Back())
	}

	return l1.Len() == 0
}
