class Solution:
    def sortVowels(self, s: str) -> str:
        t = list(s)
        w = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for ch in t:
            if ch not in w:
                continue 

            w[ch] += 1

        buffer = sorted([k, v] for k, v in w.items() if v > 0)

        j = 0
        for i, ch in enumerate(t):
            if ch not in w:
                continue

            while buffer[j][1] == 0:
                j += 1
            t[i] = buffer[j][0]
            buffer[j][1] -= 1

        return ''.join(t)

            