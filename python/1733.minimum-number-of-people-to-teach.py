

class Solution:
    def minimumTeachings(
        self, n: int, languages: list[list[int]], friendships: list[list[int]]
    ) -> int:
        langs = list(map(set, languages))
        common = [0] * (n + 1)
        count = [False] * len(languages)
        total = 0

        for u, v in friendships:
            if set(langs[u - 1]) & set(langs[v - 1]):
                continue

            count[u - 1] = True
            count[v - 1] = True

        for v, vis in enumerate(count):
            if not vis:
                continue

            total += 1

            for lang in langs[v]:
                common[lang] += 1

        return total - max(common)

