# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0 
        while curr and curr.next:
            count += 1
            curr = curr.next
        
        if n - 1 > count:
            return None
        
        if count == n - 1:
            head = head.next
            return head
        
        curr = head
        i = 0
        while curr and curr.next:
            tmp = curr.next
            if i == count - n:
                curr.next = curr.next.next
            i += 1
            curr = curr.next

        return head

        