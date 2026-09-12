class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        first = head
        sec = head.next
        prev = None

        while first is not None and sec is not None:
            third = sec.next
            sec.next = first
            first.next = third

            if prev is not None:
                prev.next = sec
            else:
                head = sec
            prev = first
            first = third
            if third is not None:
                sec = third.next
            else:
                sec = None
        return head