type Key [26]int

func groupAnagrams(strs []string) [][]string {
    groups := make(map[Key][]string)

    hasher := func(s string) Key {
        v := Key{}
        for i := range s {
            v[s[i] - 'a']++
        }

        return v
    }

    for _, word := range strs {
        key := hasher(word)
        groups[key] = append(groups[key], word)
    }

    result := make([][]string, 0, len(groups))
    for _, g := range groups {
        result = append(result, g)
    }

    return result
}