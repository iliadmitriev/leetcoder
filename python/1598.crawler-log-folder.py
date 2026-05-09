class Solution:
    def minOperations(self, logs: list[str]) -> int:
        path = 0
        for log in logs:
            if log == "../":
                if path:
                    path -= 1
            elif log != "./":
                path += 1

        return path

