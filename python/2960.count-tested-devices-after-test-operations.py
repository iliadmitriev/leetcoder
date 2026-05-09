class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        discharge = 0
        devices = 0

        for charge in batteryPercentages:
            if charge > discharge:
                devices += 1
                discharge += 1

        return devices

