class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        prefix = 0
        prev_xor_cnt = defaultdict(int)  # how many times we have seen a given prefix
        prev_xor_cnt[0] = 1
        prev_xor_index_sum = defaultdict(int)  # type: dict[int, int]

        for i in range(n):
            prefix ^= arr[i]

            if prev_xor_cnt[prefix]:
                count += i * prev_xor_cnt[prefix] - prev_xor_index_sum[prefix]

            prev_xor_cnt[prefix] += 1
            prev_xor_index_sum[prefix] += i + 1
        return count

