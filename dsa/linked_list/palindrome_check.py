# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        ## Step 1: Find the middle (stops at the first middle for even lengths)
        mid_node = self.getMid(head)
        
        ## Step 2: Get the head_2
        head_2 = mid_node.next
        
        ## Step 3: Break into 2 LL's
        mid_node.next = None
        
        ## Step 4: Reverse H2
        head_2 = self.reverseLL(head_2)
        
        head_1 = head
        while head_1 is not None and head_2 is not None:
            if head_1.val != head_2.val:
                return False
            head_1 = head_1.next
            head_2 = head_2.next
        return True

    def getMid(self, head):
        fast = head
        slow = head
        # Stops one step earlier to get the first middle node for even-length lists
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseLL(self, head):
        curr = head
        prev = None
        while curr is not None:
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
        return prev

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
    
    # Test Case 1: [1, 2] (Should be False)
    head1 = ListNode(1, ListNode(2))
    print("Test 1 List:")
    printList(head1)
    print(f"Is Palindrome? {sol.isPalindrome(head1)}") # Returns False
    
    print("-" * 40)
    
    # Test Case 2: [1, 2, 2, 1] (Should be True)
    head2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print("Test 2 List:")
    printList(head2)
    print(f"Is Palindrome? {sol.isPalindrome(head2)}") # Returns True