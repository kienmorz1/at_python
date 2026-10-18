# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dh = ListNode(-1)
        dt = dh
        
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                dt.next = list2
                list2 = list2.next
            else:
                dt.next = list1
                list1 = list1.next
            dt = dt.next
            
        if list1 is not None:
            dt.next = list1
        elif list2 is not None:
            dt.next = list2
            
        return dh.next


# --- Helper functions to test with example data ---

def create_linked_list(arr):
    """Converts a Python list to a singly-linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    """Converts a singly-linked list back to a Python list for easy printing."""
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr


# --- Example Test Run ---
if __name__ == "__main__":
    # Example input data
    raw_list1 = [1, 2, 4]
    raw_list2 = [1, 3, 4]

    # Convert standard Python lists to linked lists
    l1 = create_linked_list(raw_list1)
    l2 = create_linked_list(raw_list2)

    # Run the solution
    solution = Solution()
    merged_head = solution.mergeTwoLists(l1, l2)

    # Print the result
    output = linked_list_to_list(merged_head)
    print("Input 1:", raw_list1)
    print("Input 2:", raw_list2)
    print("Merged Output:", output)