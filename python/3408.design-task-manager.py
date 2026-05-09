import heapq


class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.tasks = []  # max heapq of tasks by priority (-priority, -userID, taskID)
        self.valid = {}  # dict of valid taskIDs -> task

        for userId, taskId, priority in tasks:
            task = (-priority, -taskId, userId)
            self.tasks.append(task)
            self.valid[-taskId] = task

        heapq.heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = (-priority, -taskId, userId)
        heapq.heappush(self.tasks, task)
        self.valid[-taskId] = task

    def edit(self, taskId: int, newPriority: int) -> None:
        oldTask = self.valid[-taskId]
        newTask = (-newPriority, oldTask[1], oldTask[2])
        self.valid[-taskId] = newTask
        heapq.heappush(self.tasks, newTask)

    def rmv(self, taskId: int) -> None:
        del self.valid[-taskId]

    def execTop(self) -> int:
        while self.tasks:
            task = heapq.heappop(self.tasks)
            _, taskId, userId = task

            # if task was removed
            if taskId not in self.valid:
                continue

            # if task was edited
            if self.valid[taskId] != task:
                continue

            del self.valid[taskId]
            return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()