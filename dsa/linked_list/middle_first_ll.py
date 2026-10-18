class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def middle(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


def create_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    middle = Solution().middle(head)
    print(middle.val if middle is not None else None)
