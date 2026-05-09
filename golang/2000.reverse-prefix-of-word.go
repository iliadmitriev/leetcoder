package main

import "strings"

func reversePrefix(word string, ch byte) string {
	pos := strings.IndexByte(word, ch)
	rev := make([]byte, 0, pos+1)
	for i := pos; i >= 0; i-- {
		rev = append(rev, word[i])
	}

	return string(rev) + word[pos+1:]
}
