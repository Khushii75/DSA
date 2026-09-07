# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # l=0
        # curr=head
        # while curr!=None:
        #     l+=1
        #     curr=curr.next
        # a=l-n #a step befor the node to be deleted.
        # curr=head
        # if a == 0:
        #     return head.next
        # cnt=1
        # while cnt < a:
        #     curr = curr.next
        #     cnt += 1

        # curr.next = curr.next.next

        # return head
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
        
      