import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Counter(tasks) - hashmap of alphabets as keys, counts as values
        form list of alphabet counts, multiply each elem by -1 and conver to maxHeap
        form queue: [count, time], count - remaining count for alphabet, next available time that alphabet can be called
        iterate through heap or queue: increment time, heappop into count,
        if count != 0: append cnt and time+n into queue
        if q and q values == time: popleft from heap

        time complexity: O(N)
        space complexity: O(N)
        """
        count: dict[int, str] = Counter(tasks)
        maxHeap: list[int] = [-num for num in count.values()]
        heapq.heapify(maxHeap)
        time: int = 0
        q: list[list[int]] = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt: int = heapq.heappop(maxHeap)
                # if cnt == 0: there is no need to append into q anymore bc the task/alphabet has been completed
                if cnt != 0:
                    q.append([cnt, time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
