# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        slow= head
        fast= head
        temp= None
        while fast is not None and fast.next is not None:
            temp= slow
            slow= slow.next
            fast= fast.next.next
        if temp==None:
            return None    
        temp.next= slow.next        
        return head