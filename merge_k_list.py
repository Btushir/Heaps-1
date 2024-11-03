import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        listpq = []
        # for all the list put the head of each list in heap
        for i, node in enumerate(lists):
            if node:
                #
                heapq.heappush(listpq, (node.val, i, node))

        dummy = ListNode(-1)
        curr = dummy

        while listpq:
            nodeVal, i, node = heapq.heappop(listpq)
            curr.next = node
            curr = curr.next
            if node.next:
                node = node.next
                heapq.heappush(listpq, (node.val, i, node))

        return dummy.next





