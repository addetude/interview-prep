# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        if not head or not head.next:
            return head

        currOne = None
        currTwo = head
        currThree = currTwo.next

        while currThree:
            currTwo.next = currOne
            currOne = currTwo
            currTwo = currThree
            currThree = currThree.next

        currTwo.next = currOne
        return currTwo

        