class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = defaultdict(int)
        for r,s in reservedSeats:
            s -= 2 # shift unused bit and make 0-based

            if s < 0 or s > 7:
                continue

            rows[r] |= 1 << s

        m1  = 0b00001111 # mask 1: 2,3,4,5
        m2  = 0b11110000 # mask 2: 6,7,8,9
        m3  = 0b00111100 # mask 3: 4,5,6,7
 
        # fill free rows optimally with 2 quater person groups
        total = (n - len(rows)) * 2

        for m in rows.values():
            if m1 & m == 0 or m2 & m == 0 or m3 & m == 0:
                total += 1

        return total

        