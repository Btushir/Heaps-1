from heapq import heappush
from heapq import heappop
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # store the frequency of each task in hmap
        hmap = {}
        for t in tasks:
            if t not in hmap:
                hmap[t] = 0
            hmap[t] += 1

        # add the frequencies of chars in max heap.
        # max heap is choosen becasue the max most frequent element
        # gives optimal result. Check ["A","C","A","B","D","B"]
        pq = []
        for key in hmap:
            heappush(pq, -1 * hmap[key])

        # to keep track of what to add and when to add
        q = deque()  # (task freq, time after which it can be added)
        time = 0
        # it is possible that heap is empty and queue is not empty
        # so we want to make sure the loop ends when both heap and queue are empty
        while pq or q:
            # get the max frequency number if pq
            if pq:
                # increment time by 1
                time += 1
                frq = heappop(pq)
                # append the left freq and time at which it can be added
                if frq + 1 < 0:
                    q.append((frq + 1, time + n))

            # check if there is element in q and current time is equal to first element of queue
            if q and q[0][1] == time:
                f, t = q.popleft()
                heappush(pq, f)

            # if pq is empty but there are tasks in queue
            # increment the time, this is idle time
            if not pq and q:
                time += 1

            # if both queue and pq are empty then stop
            if not pq and not q:
                break

        return time

