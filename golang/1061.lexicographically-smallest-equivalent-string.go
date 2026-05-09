type ChrUFind struct {
	par []byte
}

func NewChrUFind() *ChrUFind {
	par := make([]byte, 26)
	for i := byte(0); i < 26; i++ {
		par[i] = i
	}

	return &ChrUFind{
		par: par,
	}
}

func (u *ChrUFind) find(x byte) byte {
	for x != u.par[x] {
		u.par[x] = u.par[u.par[x]]
		x = u.par[x]
	}

	return x
}

func (u *ChrUFind) join(x, y byte) {
	px, py := u.find(x), u.find(y)

	switch {
	case px == py:
		return
	case px < py:
		u.par[py] = px
	default:
		u.par[px] = py
	}
}

func (u *ChrUFind) findBased(ch byte) byte {
	return 'a' + u.find(ch-'a')
}

func (u *ChrUFind) joinBased(ch1, ch2 byte) {
	u.join(ch1-'a', ch2-'a')
}

func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
	uf := NewChrUFind()

	for i := range s1 {
		uf.joinBased(s1[i], s2[i])
	}

	res := make([]byte, len(baseStr))
	for i := range baseStr {
		res[i] = uf.findBased(baseStr[i])
	}

	return string(res)
}
