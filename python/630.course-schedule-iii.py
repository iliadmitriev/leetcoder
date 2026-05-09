class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """Prority queue.
        
        Use priority queue to store duration.
        
        Algorithm:
        1. Start learining courses from earliest closing date (sort by end time)
        2. Count overall time
        3. Learn first course.
        4. Check if it can be fit in closing date
        5. Unlearn largest course if it doesn't fit
        
        Time: O(n * log n)
        Space: O(n)
        """
        queue = []
        time = 0
        for duration, end_time in sorted(courses, key=lambda x: x[1]):
            # learn course
            heapq.heappush(queue, -duration)
            time += duration
            # check if we finish later than course end time
            if time > end_time:
                # unlearn course (decrease overall time by biggest course from queue)
                time += heapq.heappop(queue)

        return len(queue)