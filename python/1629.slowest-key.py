class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:

        prev = 0
        maxDur = 0
        maxDurKey = keysPressed[0]

        for tm, key in zip(releaseTimes, keysPressed):
            duration = tm - prev
            prev = tm

            if duration > maxDur or duration == maxDur and key > maxDurKey:
                maxDur = duration
                maxDurKey = key

        return maxDurKey

