func removeDuplicateLetters(s string) string {
    added := make([]bool, 26)
    stack := make([]rune, 26)
    top := -1
    last := make([]int, 26)
    for i, ch := range s { last[ch - 'a'] = i }

    for i, ch := range s {
        if added[ch - 'a'] {
            continue;
        }

        for top != -1 && ch < stack[top] && i < last[stack[top] - 'a'] {
            added[stack[top] - 'a'] = false;
            top--;
        }

        added[ch - 'a'] = true;
        top++;
        stack[top] = ch;
    }

    return string(stack[:top + 1]);
}