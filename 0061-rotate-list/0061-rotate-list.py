# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        curr=head
        last=head
        if head==None:
            return head
        while last.next!=None:
            last= last.next
            l+=1
        l+=1
        k=k%l

        if k==0:
            return head
      
        for i in range(l-k-1):
            curr=curr.next
        last.next=head
        head=curr.next
        curr.next=None
        return head
        



        