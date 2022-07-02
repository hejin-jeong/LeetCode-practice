# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        
        dum = ListNode("dum")
        dum.next = head
        odd = head
        even = head.next
        even_head = head.next
        
        while odd.next and even.next:
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            
            if even.next.next:
                even.next = even.next.next
                even = even.next
        
        odd.next = None
        even.next = None
        odd.next = even_head
        
        return dum.next
            
        