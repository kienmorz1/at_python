# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        return slow

# Helper function to print the linked list
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
    
    # Test Case 1: Odd-length linked list (1 -> 2 -> 3 -> 4 -> 5)
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List 1 (Odd Length):")
    printList(head1)
    
    mid1 = sol.middleNode(head1)
    print(f"Middle Node Value: {mid1.val}")
    print("From Middle Onward:")
    printList(mid1)
    
    print("-" * 40)
    
    # Test Case 2: Even-length linked list (1 -> 2 -> 3 -> 4 -> 5 -> 6)
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print("Original List 2 (Even Length):")
    printList(head2)
    
    mid2 = sol.middleNode(head2)
    print(f"Middle Node Value (Second Middle): {mid2.val}")
    print("From Middle Onward:")
    printList(mid2)