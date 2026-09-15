# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow= head
        fast= head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
        prev= None
        curr= slow
        while curr is not None:
            next= curr.next
            curr.next= prev
            prev= curr
            curr= next
        p= head
        q= prev
        while q is not None:
            if p.val!=q.val:
                return False
            p= p.next
            q= q.next
        return True        