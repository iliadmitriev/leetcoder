class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # move heavy asteroids to the beggining
        h = 0  # heavy index

        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                asteroids[h] = a
                h += 1

        asteroids = asteroids[:h]
        asteroids.sort()

        for a in asteroids:
            if mass < a:
                return False

            mass += a

        return True
