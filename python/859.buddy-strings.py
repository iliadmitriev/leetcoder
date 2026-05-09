class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        swaps = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                swaps.append((s[i], goal[i]))
            if len(swaps) > 2:
                return False

        return len(swaps) == 2 and swaps[0] == swaps[1][::-1]