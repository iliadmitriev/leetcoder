func isPalindrome(s string) bool {
    isAlphaNum := func (b byte) bool {
        if '0' <= b && b <= '9' {
            return true
        }

        if 'A' <= b && b <= 'Z' {
            return true
        }

        if 'a' <= b && b <= 'z' {
            return true
        }

        return false
    } 

    toLower := func (b byte) byte {
        if 'A' <= b && b <= 'Z' {
            return b + 32
        }
        
        return b
    }

    for i, j := 0, len(s) - 1; i < j; i, j = i + 1, j - 1 {
        for i < j && !isAlphaNum(s[i]) {
            i++
        }

        for i < j && !isAlphaNum(s[j]) {
            j--
        }

        if toLower(s[i]) != toLower(s[j]) {
            return false
        }
    }

    return true
}