import (
	"strings"
)

type letterItem struct {
	ch  byte
	cnt int
}

type letters []letterItem

func (l *letters) Append(b byte, cnt int) {
	*l = append(*l, letterItem{b, cnt})
}

func (l *letters) Pop() (byte, int) {
	v := (*l)[len(*l)-1]
	(*l) = (*l)[:len(*l)-1]
	return v.ch, v.cnt
}

func (l *letters) Empty() bool {
	return len(*l) == 0
}

type Repetition struct {
	strings.Builder
}

func (r *Repetition) WriteBytes(b byte, cnt int) {
	for i := 0; i < cnt; i++ {
		r.WriteByte(b)
	}
}

func repeatLimitedString(s string, repeatLimit int) string {
	freq := make([]int, 26)
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}

	letters := make(letters, 0)
	for i := 0; i < len(freq); i++ {
		if freq[i] > 0 {
			letters.Append(byte('a'+i), freq[i])
		}
	}

	res := Repetition{}

	for !letters.Empty() {
		ch, cnt := letters.Pop()

		if cnt > repeatLimit {

			cnt -= repeatLimit
			res.WriteBytes(ch, repeatLimit)

			if letters.Empty() {
				break
			}

			nextCh, nextCnt := letters.Pop()
			res.WriteByte(nextCh)
			nextCnt--

			if nextCnt > 0 {
				letters.Append(nextCh, nextCnt)
			}
			letters.Append(ch, cnt)

		} else {
			res.WriteBytes(ch, cnt)
		}
	}

	return res.String()
}
