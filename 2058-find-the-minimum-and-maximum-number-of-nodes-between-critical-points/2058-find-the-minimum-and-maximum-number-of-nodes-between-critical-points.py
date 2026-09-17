# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crits = []
        prev = None
        cur = head
        index = 1
        while cur != None:
            if prev != None and cur.next != None:
                if (prev.val > cur.val and cur.next.val > cur.val) or (prev.val < cur.val and cur.next.val < cur.val):
                    crits.append(index)
            prev = cur
            cur = cur.next
            index += 1
        if len(crits) < 2:
            return [-1,-1]
        largest = crits[-1] - crits[0]
        smallest = crits[1]-crits[0]
        for i in range(2, len(crits)):
            smallest = min(crits[i]-crits[i-1], smallest)
        return [smallest,largest]
        


        
        