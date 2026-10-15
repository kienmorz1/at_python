# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
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
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    print("Original List:")
    printList(head)
    
    # Reversing the list
    sol = Solution()
    reversed_head = sol.reverseList(head)
    
    print("Reversed List:")
    printList(reversed_head)