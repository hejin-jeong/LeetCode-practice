# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 1:
            return head

        dum = ListNode("dummy")
        dum.next = head
        pre = dum
        s = head
        p = head.next

        ll_len = 1
        temp = head
        while temp.next:
            temp = temp.next
            ll_len += 1

        iteration_count = 0
        while iteration_count < ll_len//k:
            c = 1
            while c < k:
                s.next = p.next
                p.next = pre.next
                pre.next = p
                p = s.next
                c += 1
            pre = s
            s = s.next
            if p:
                p = p.next
            iteration_count += 1

        return dum.next
