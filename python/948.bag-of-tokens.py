class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # sort tokens ascending
        tokens.sort()
        # two pointers tecnique:
        # left pointer for getting smallest values
        # it's more profitable to spend smallest values to get scores
        # right pointer for getting largest values
        # it's more profitable to spend scores to get biggest tokens for power
        left, right = 0, len(tokens) - 1
        # result 
        ans = 0
        # current scores
        score = 0
        while right >= left:
            # if there is enough power get scores
            # spending power for tokens (left part of list)
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                # calculate result
                ans = max(ans, score)
            # if there is not enough power and is still some scores
            # get power spending score for tokens (from right part of list)
            elif score > 0 and power < tokens[left]:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                # if there's no score and not enough power to get scores
                # just finish earlier and return answer
                # (without left and right pointers meeting)
                break
        
        return ans