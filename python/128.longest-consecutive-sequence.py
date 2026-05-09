class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numsSet = set(nums)
        maxLength = 0

        for num in numsSet:
            # skip it's it's not the start of the sequence
            if num - 1 in numsSet:
                continue

            # find all consecutive numbers
            temp = num
            while temp + 1 in numsSet:
                temp += 1
            maxLength = max(maxLength, temp - num + 1)

            # if current sequnce length is greater than a half of the array
            # then it's impossible to find another sequence with greater length
            if maxLength > len(nums) // 2:
                break

        return maxLength

