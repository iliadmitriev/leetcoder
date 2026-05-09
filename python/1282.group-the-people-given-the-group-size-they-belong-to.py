class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        assigned = []

        for person, group_cap in enumerate(groupSizes):
            
            groups[group_cap].append(person)

            if len(groups[group_cap]) == group_cap:
                assigned.append(groups.pop(group_cap))
                
        return assigned
        