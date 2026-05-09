class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxSeq = 0
        l1, l2, r = 0, 0, 0
        k1, k2 = k, k

        for r in range(len(answerKey)):
            k1 -= int(answerKey[r] == "T")
            k2 -= int(answerKey[r] == "F")

            if k1 < 0:
                k1 += int(answerKey[l1] == "T")
                l1 += 1

            if k2 < 0:
                k2 += int(answerKey[l2] == "F")
                l2 += 1

            maxSeq = max(maxSeq, r - l1 + 1, r - l2 + 1)

        return maxSeq

