# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the length of the list
        n = 1
        node = head
        while node.next:
            n += 1
            node = node.next

        # 2. Advance node_i to the node JUST BEFORE the second half starts
        node_i = head
        i = 0
        while i < (n // 2) - 1:  # Use integer division
            node_i = node_i.next
            i += 1
            
        # 3. Reverse the second half of the list
        node_j = node_i.next
        prev = None  
        
        while node_j:
            tmp = node_j.next
            node_j.next = prev
            prev = node_j
            node_j = tmp
            
        # prev is now the head of the reversed second half
        node_i = prev 

        # 4. Calculate the max twin sum
        max_sum = 0
        i = 0
        node = head
        
        while i < (n // 2):  # Use integer division
            max_sum = max(node_i.val + node.val, max_sum)
            node_i = node_i.next
            node = node.next
            i += 1

        return max_sum