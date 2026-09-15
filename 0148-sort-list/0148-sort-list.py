# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        slow= head
        fast= head
        temp= None
        while fast is not None and fast.next is not None:
            temp= slow
            slow= slow.next
            fast= fast.next.next
        temp.next=None    
        left= self.sortList(head)
        right= self.sortList(slow)
        dummy= ListNode(0)
        curr= dummy
        while left is not None and right is not None:
            if left.val<right.val:
                curr.next= left
                left= left.next
            else:
                curr.next= right
                right= right.next
            curr= curr.next
        if left is None:
            curr.next = right
        else: 
            curr.next= left
        return dummy.next    
             
       