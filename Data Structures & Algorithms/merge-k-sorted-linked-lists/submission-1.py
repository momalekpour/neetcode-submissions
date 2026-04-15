# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ## Solution 1: time O(n * k), space O(1)
        ## which n is number of total nodes and k number of lists
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.merge_two_lists(lists[i-1], lists[i])

        return lists[-1]

    def merge_two_lists(self, h1, h2):
        curr1, curr2 = h1, h2
        dummy = ListNode(-1, None)
        curr = dummy
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
    
        return dummy.next
