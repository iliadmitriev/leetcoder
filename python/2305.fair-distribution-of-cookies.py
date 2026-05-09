import itertools as it


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # n = len(cookies)
        # res = float("inf")
        # for comb in it.product(range(k), repeat=n):
        #     total = defaultdict(int)
        #     for i, p in enumerate(comb):
        #         total[p] += cookies[i]
        #     res = min(res, max(total.values()))

        # return res

        
        # sort cookie in descending order
        # biggest cookies fisrt
        cookies.sort(reverse=True)
        # calculate maximum limit
        heap = [0] * k
        for i in cookies:
            p = heapq.heappop(heap)
            p += i
            heapq.heappush(heap,p)
        cur_max = max(heap)        

        def backtrack(people, c_id):  
            nonlocal cur_max          
            if c_id == len(cookies):
                cur_max = min(cur_max, max(people))
                return

            # for all the people try to add current cookie with c_id
            # without exceeding a limit
            for p in range(len(people)):
                # if current person can get a cookie without exceeding the limit
                # then it could be one of possible combiantions
                if people[p] + cookies[c_id] < cur_max:
                    # start backtracking
                    people[p] += cookies[c_id]
                    backtrack(people.copy(), c_id + 1)
                    people[p] -= cookies[c_id]

        backtrack([0] * k, 0)
        return cur_max