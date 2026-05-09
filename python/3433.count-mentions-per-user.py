
MESSAGE = "MESSAGE"
OFFLINE = "OFFLINE"

MENTION_ALL = "ALL"
MENTION_HERE = "HERE"
MENTION_SEP = " "

OFFLINE_PERIOD = 60


class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        # n - number of events
        # m - number of users
        # Space: O(m)
        offline_time = [0] * numberOfUsers
        mentions = [0] * numberOfUsers

        def get_user_ids(inp: str) -> list[int]:
            usr = list()
            for us in inp.split(MENTION_SEP):
                id_ = int(us[2:])
                usr.append(id_)

            return list(usr)

        # Time: O(n * log(n) * log(m))
        events.sort(key=lambda x: (int(x[1]), x[0] == MESSAGE))

        # Time: O(n * m)
        for ev_type, ts, mention_list in events:
            timestamp = int(ts)

            if ev_type == MESSAGE:
                if mention_list == MENTION_ALL:
                    for id_ in range(numberOfUsers):
                        mentions[id_] += 1
                elif mention_list == MENTION_HERE:
                    for id_ in range(numberOfUsers):
                        if offline_time[id_] <= timestamp:
                            mentions[id_] += 1
                else:
                    for id_ in get_user_ids(mention_list):
                        mentions[id_] += 1

            elif ev_type == OFFLINE:
                id_ = int(mention_list)
                offline_time[id_] = timestamp + OFFLINE_PERIOD

        return mentions

