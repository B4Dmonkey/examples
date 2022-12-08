from typing import Optional


class ListNode:
  def __init__(self,val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0 
    ans = None

    while l1 or l2:
      l1_val = l1.val if l1 else 0
      l2_val = l2.val if l2 else 0
      
      pos_sum = l1_val + l2_val + carry
      carry = 0 

      if pos_sum >= 10:
        pos_sum %= 10
        carry = 1
      
      ans = ListNode(pos_sum, ans)
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None

    return ans
