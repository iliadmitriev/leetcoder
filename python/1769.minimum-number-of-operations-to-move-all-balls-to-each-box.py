class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        res = [0] * n
        leftCnt, rightCnt = 0, boxes.count("1")
        leftSum, rightSum = 0, sum(i + 1 for i in range(n) if boxes[i] == "1")

        for i in range(n):
            rightSum -= rightCnt
            rightCnt -= int(boxes[i] == "1")
            leftCnt += int(boxes[i] == "1")

            res[i] = leftSum + rightSum
            leftSum += leftCnt

        return res

