# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        set = {head}
        while head.next:
            head = head.next
            if head not in set:
                set.add(head)
            else:
                return True

        return False
        