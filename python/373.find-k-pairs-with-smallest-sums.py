from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        
        res = []
        pq = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()

        while pq and k:
            _, p1, p2 = heappop(pq)
            res.append([nums1[p1], nums2[p2]])

            if p1 + 1 < n1 and (p1 + 1, p2) not in visited:
                heappush(pq, (nums1[p1 + 1] + nums2[p2], p1 + 1, p2))
                visited.add((p1 + 1, p2))
            
            if p2 + 1 < n2 and (p1, p2 + 1) not in visited:
                heappush(pq, (nums1[p1] + nums2[p2 + 1], p1, p2 + 1))
                visited.add((p1, p2 + 1))

            k -= 1

        return res

            
