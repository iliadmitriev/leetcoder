var mp = map[byte][]string{
    '2': {"a", "b", "c"},
    '3': {"d", "e", "f"},
    '4': {"g", "h", "i"},
    '5': {"j", "k", "l"},
    '6': {"m", "n", "o"},
    '7': {"p", "q", "r", "s"},
    '8': {"t", "u", "v"},
    '9': {"w", "x", "y", "z"},
}

func dfs(curr string, res *[]string, i int, digits string) {
    if i == len(digits) {
        *res = append(*res, curr)
        return
    }
    for _, ch := range mp[digits[i]] {
        dfs(curr + ch, res, i + 1, digits)
    }
}

func letterCombinations(digits string) []string {
   var res []string
    if digits == "" {
        return res
    }

    dfs("", &res, 0, digits)
    return res
}