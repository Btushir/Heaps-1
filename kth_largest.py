"""
Heap sort does not guarantee the oder of duplicates thus under the hood, sorting is done using merge sort, since it
maintains the order of duplicates. To make it work add priority.

Approach1: maintain a heap: maintain a max heap: n log(n) to add to heap + k log(n) to remove from heap
Approach2: maintain a min heap of size k+1, when a number comes in when size is greater than k, for example, k = 4
[2,3,4,5] and 1 comes in it can not be among the kth largest element this is because any number greater than 1 can be
among kth largest and number less than 1 and 1 can not among kth largest. so pop 1.
Whatever is at the top is kth largest.
TC: using heap: n (log(k) for inserting + log(k) for pop)
"""

from heapq import heappush as insert
from heapq import heappop as remove


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # define the list that would be heap
        heap = []

        # traverse the array
        for num in nums:
            # add element to heap until lenght k
            if len(heap) < k:
                insert(heap, num)
            else:
                # any number less than root of heap will not part of
                # kth largest, and number greater than root may be part
                # thus compares root with num and if greater insert it
                # and to maintain size k pop.
                if num > heap[0]:
                    insert(heap, num)
                    remove(heap)

        return heap[0]