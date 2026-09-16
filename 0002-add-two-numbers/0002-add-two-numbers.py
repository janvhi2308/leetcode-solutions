# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry=0
        dummy= ListNode(0)
        curr= dummy
        while l1 is not None or l2 is not None or carry !=0:
            if l1 is not None:
                v1= l1.val
            else:
                v1=0
            if l2 is not None:
                v2= l2.val
            else:
                v2=0            
            res= v1+v2 + carry
            digit= res%10
            carry=res//10
            curr.next= ListNode(digit)
            curr= curr.next
            if l1 is not None:
                l1= l1.next
            if l2 is not None:
                l2= l2.next
        return dummy.next       
        