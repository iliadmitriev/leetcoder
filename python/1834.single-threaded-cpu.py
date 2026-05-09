from heapq import heappop, heappush, heapify


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """Single-Threaded CPU.
        
        https://en.wikipedia.org/wiki/Shortest_job_next

        Two heap queues.

        job data:
            - enque time (ready, start) - time when job is ready to start
            - process time (work, process) - time needed to process job (enque time + process time = finish time)

        1. put jobs to task queue, with tuples (ready, work, index)
        2. init empty list of waiting jobs
        3. while there is tasks in ready and wating job lists
            - if there is job a ready job wating - then take it
                * get it process time (start processing it, encrease elapsed time by a process time)
            - otherwise (if there is no ready jobs, then you have to wait for the first upcoming job to be ready):
                * set elapsed time to a job ending time
            - put job to the worker thread (to the result)
            - look for a ready jobs from the job queue (job time is less or equal to current time elapsed)
                * pop job from jobs queue and push it to the ready queue

        """
        jobs = [(start, process, index) for index, (start, process) in enumerate(tasks)]
        heapify(jobs)
        ready = []
        thread = []
        while jobs or ready:
            if ready:
                process, idx = heappop(ready)
                elapsed += process
            else:
                start, process, idx = heappop(jobs)
                elapsed = start + process
            thread.append(idx)
            while jobs and jobs[0][0] <= elapsed:
                _, process, idx = heappop(jobs)
                heappush(ready, (process, idx))
        return thread