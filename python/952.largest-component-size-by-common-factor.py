@cache
def prime_factors_2(n: int) -> set[int]:  # Prime factor decomposition
    out = set()
    while n % 2 == 0:
        out.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            out.add(i)
            n //= i
    if n > 2:
        out.add(n)
    return out


class Solution:

    def largestComponentSize(self, nums: List[int]) -> int:
        """Calculates the largest component size by common factor

        From give list of numbers representing vertices of graph
        find largest component. Graph undirected edge exists if
        there is common factor between two vertices greater than 1

        :param nums: list of unique numbers representing graph vertices
        :return: length of greatest component
        """

        primes = defaultdict(set)
        vert = defaultdict(set)
        # first calculate
        # mapping from prime -> set of vertices (which has prime as a factor)
        # mapping from vertex -> set of primes (which it has as factors)
        for num in nums:
            for i in prime_factors_2(num):
                primes[i].add(num)
                vert[num].add(i)

        max_length = 0
        queue = set()
        # our goal is to merge all the connected vertices in graph components
        # then decide which of components is larger
        # and return its length
        # all the vertices in prime values are already connected
        # they are subsets of bigger components
        while primes:
            # this is our component (set of connected vertices)
            res = set()
            # get next set of connected vertices
            _, values = primes.popitem()
            # add this set to queue
            queue.update(values)
            while queue:
                # get vertex from queue
                curr = queue.pop()
                # add vertex to result
                res.add(curr)
                # get vertex prime factors
                for k in vert[curr]:
                    # check if we already merged this prime number vertices
                    # to current component res
                    if k in primes:
                        # add to queue all vertices from prime number
                        queue.update(primes[k])
                        # and delete all vertices from prime number key
                        # we don't need it since it's added to queue
                        # and will be merged to current component
                        del primes[k]
            # check if current component is greater than previous
            max_length = max(max_length, len(res))

        return max_length
