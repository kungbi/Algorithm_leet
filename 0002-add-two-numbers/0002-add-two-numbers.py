# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        tmp = result
        while (l1 or l2):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0 
            sum = l1_val + l2_val + tmp.val

            tmp.val = sum % 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if sum//10 or (l1 or l2):
                tmp.next = ListNode(val=sum//10)
                tmp = tmp.next


        return result