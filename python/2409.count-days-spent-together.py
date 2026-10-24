from datetime import datetime as dt

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def day_of_year(s: str) -> int:
            return dt.strptime(s, "%m-%d").timetuple().tm_yday
        
        arrive = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        leave = min(day_of_year(leaveAlice), day_of_year(leaveBob)) + 1
        
        return max(0, leave - arrive)