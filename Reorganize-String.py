from heapq import heappush
from heapq import heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        hq = []

        #  store all the char along with their frequency in hmap.
        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 0
            hmap[c] += 1
        # create max heap
        pq = []
        for ch, count in hmap.items():
            # pyton heap heapify using the first value and if tie heapify using 2nd element
            heappush(pq, (-1*count, ch))

        # keep track of previous
        prev = None
        ans = []
        while pq:
            # get the most frequent element of heap.
            count, ch = heappop(pq)
            # add it to the response 
            ans.append(ch)

            # if previous exists, add it to the heap
            # this make sure the same element is not appened twice continuously 
            if prev:
                heappush(pq, prev)
                prev = None 

            # update count and and only update previous if count < 0
            # Do not push element if it cout is zero
            count += 1
            if count < 0:
                prev = (count, ch)
               
        print(ans)
        if len(ans) == len(s):
            return "".join(ans)
        else:
            return ""
        

        