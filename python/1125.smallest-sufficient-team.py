import operator
from functools import reduce


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m, n = len(req_skills), len(people)
        # map from skill_name to skill_id
        skill_id = {skill: i for i, skill in enumerate(req_skills)}
        skill_bit = lambda x: 1 << skill_id[x]

        # person skills masks (no skills 0x000, all skills 0x111)
        person_skills = [reduce(operator.or_, map(skill_bit, skills), 0) for skills in people]

        # dp[i] = 0x111 * (2^m - 1)
        # dp maps from needed skill mask => to taken people mask
        # initially we take all people for every combination of skills
        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0

        for skill_mask in range(1, 1 << m):
            for i in range(n):
                smaller_skill_mask = skill_mask & ~person_skills[i]
                if smaller_skill_mask != skill_mask:
                    people_mask = dp[smaller_skill_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skill_mask].bit_count():
                        dp[skill_mask] = people_mask

        res_mask = dp[(1 << m) - 1]
        res = [i for i in range(n) if (res_mask >> i) & 1]

        return res