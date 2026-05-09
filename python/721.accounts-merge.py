# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# https://cp-algorithms.com/data_structures/disjoint_set_union.html
class DSU(object):
    """Disjoint Union Set (Union find)"""
    def __init__(self, size: int):
        """Create disjoint union set in list
        initialized by vertices themself 0..size-1

        :param size: size of disjoint set (number of vertices)
        """
        # size of each disjoint set is equal to 1
        self.size = [1] * size
        # all the representatives point to themself
        self.repr = [x for x in range(size)]

    def find(self, x: int) -> int:
        """Find vertex representative group

        :param x: vertex to find
        :return: vertex index which represents group
        """
        # while we haven't found
        # our vertex representative set
        while x != self.repr[x]:
            # path compression optimization
            self.repr[x] = self.repr[self.repr[x]]
            # next step
            x = self.repr[x]

        return self.repr[x]

    def union(self, x: int, y: int):
        """Merge two specified sets
        (the set in which element a located,
         and the set which element b located)
         Algorithm chooses biggest set and merges
         smallest set into it

        :param x: element representing first set
        :param y: element representing second set
        :return:
        """
        # find representatives of x and y
        x_repr = self.find(x)
        y_repr = self.find(y)
        # if representative points to one group then
        # they are already merged (we do nothing)
        if x_repr == y_repr:
            return
        else:
            # choose the set group with biggest size
            if self.size[x_repr] > self.size[y_repr]:
                # biggest x_repr
                # we merge y_repr to it
                self.size[x_repr] += self.size[y_repr]
                self.size[y_repr] = 0
                self.repr[y_repr] = x_repr
            else:
                # biggest y_repr
                # we merge x_repr to it
                self.size[y_repr] += self.size[x_repr]
                self.size[x_repr] = 0
                self.repr[x_repr] = y_repr


class Solution:
    """Solution using disjoint sets (union find)"""

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Merge given account records by email address

                    name       first address       second address
                    |          |                   |
        account: [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                 ["John", "johnsmith@mail.com", "john00@mail.com"]]

        res: [["John", "johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]]

        Steps:
            1. create DSU with size of accounts list
            2. map email to their component index `email_group[email] = index`
                * if email is not in email_group => add it
                * else merge email index with account group index
            3. save email corresponding to their components using dsu:
                components[group_representative] -> emails list
            4. sort and compile result,
                add name from accounts[group_representative][0]

        :param accounts: list of account emails
        :return: list of account email with removed duplicates
        """
        dsu = DSU(size=len(accounts))
        email_group = defaultdict(int)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in email_group:
                    # if we have seen this email account[j]
                    # than merge its group and current group
                    dsu.union(i, dsu.find(email_group[account[j]]))
                else:
                    email_group[account[j]] = i

        components = defaultdict(list)
        for email in email_group:
            group = email_group[email]
            group_repr = dsu.find(group)
            components[group_repr].append(email)

        res = []
        for group in components:
            component = components[group]
            res.append([accounts[group][0]] + sorted(component))

        return res

