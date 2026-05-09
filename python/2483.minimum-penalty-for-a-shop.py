class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total_penalty = customers.count("Y")

        min_penalty = total_penalty
        cur_penalty = total_penalty
        earliestHour = 0

        for i, b in enumerate(customers, start=1):
            cur_penalty += 1 if b == "N" else -1

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                earliestHour = i

        return earliestHour

