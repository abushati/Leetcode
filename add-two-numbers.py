# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            root = ListNode()
            next_pointer = root
            carry = 0
            while True:
                if l1 is None:
                    l1_val = 0
                else:
                    l1_val = l1.val
                    l1 = l1.next
                    
                if l2 is None:
                    l2_val = 0
                else:
                    l2_val = l2.val
                    l2 = l2.next
                
                value = l1_val + l2_val + carry
                if value >= 10:
                    if value == 10:
                        next_pointer.val = 0
                    else:
                        next_pointer.val = value % 10
                    carry = 1
                else:
                    carry = 0
                    next_pointer.val = value
                
                if l1 is None and l2 is None and carry == 0:
                    break 
                
                next_pointer.next = ListNode()
                next_pointer = next_pointer.next
                
            
            return root