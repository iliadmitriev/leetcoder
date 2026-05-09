from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        recipesHash = set(recipes)
        adj = defaultdict(list)
        inorder = defaultdict(int)
        done = []

        for _to, _froms in zip(recipes, ingredients):
            for _from in _froms:
                adj[_from].append(_to)
                inorder[_to] += 1

        q = deque(supplies)

        while q:
            cur = q.popleft()
            if cur in done:
                continue

            if cur in recipesHash:
                done.append(cur)

            if cur not in adj:
                continue

            for n in adj[cur]:
                inorder[n] -= 1

                if inorder[n] == 0:
                    q.append(n)

        return done

