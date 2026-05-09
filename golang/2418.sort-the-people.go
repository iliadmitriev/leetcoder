type Person struct {
	Name   string
	Height int
}

type ByHeight []Person

func (b ByHeight) Len() int {
	return len(b)
}

func (b ByHeight) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func (b ByHeight) Less(i, j int) bool {
	return b[i].Height > b[j].Height
}

func sortPeople(names []string, heights []int) []string {
	tmp := make([]Person, 0, len(heights))
	for i := 0; i < len(heights); i++ {
		tmp = append(tmp, Person{Name: names[i], Height: heights[i]})
	}

	sort.Sort(ByHeight(tmp))

	ret := make([]string, len(tmp))
	for i := 0; i < len(tmp); i++ {
		ret[i] = tmp[i].Name
	}
	return ret
}
