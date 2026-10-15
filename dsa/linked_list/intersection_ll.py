# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head2: ListNode
        :rtype: ListNode
        """
        s1 = self.getSize(headA)
        s2 = self.getSize(headB)
        if s1 > s2:
            diff = s1 - s2
            while diff > 0:
                diff -= 1
                headA = headA.next
        else:
            diff = s2 - s1
            while diff > 0:
                diff -= 1
                headB = headB.next
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA

    def getSize(self, head):
        temp = head
        c = 0
        while temp is not None:
            c += 1
            temp = temp.next
        return c

# Helper function to print a list
def printList(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res))

# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    
    # Create intersecting tail: 8 -> 4 -> 5
    common_tail = ListNode(8)
    common_tail.next = ListNode(4)
    common_tail.next.next = ListNode(5)
    
    # Create List A: 4 -> 1 -> (common_tail)
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common_tail
    
    # Create List B: 5 -> 6 -> 1 -> (common_tail)
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common_tail
    
    print("List A:")
    printList(headA)
    
    print("List B:")
    printList(headB)
    
    # Find intersection
    intersection = sol.getIntersectionNode(headA, headB)
    
    if intersection:
        print(f"\nIntersection found at node with value: {intersection.val}")
    else:
        print("\nNo intersection found.")