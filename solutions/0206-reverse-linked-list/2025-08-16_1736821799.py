# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        if not head.next:
            return head
        
        one = None
        two = head

        while two:
            nex = two.next
            two.next = one
            one = two
            two = nex
        
        return one
        