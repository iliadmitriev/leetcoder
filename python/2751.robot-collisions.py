

class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        st: list[int] = []
        idx = sorted(range(len(positions)), key=positions.__getitem__)

        for pos in idx:
            while (
                st
                and directions[st[-1]] == "R"
                and directions[pos] == "L"
                and healths[pos] > 0
            ):
                i = st.pop()
                if healths[i] > healths[pos]:
                    healths[i] -= 1
                    healths[pos] = 0
                    pos = i
                    break
                elif healths[i] < healths[pos]:
                    healths[i] = 0
                    healths[pos] -= 1
                else:
                    healths[pos] = healths[i] = 0

            if healths[pos] > 0:
                st.append(pos)

        return [health for health in healths if health > 0]

