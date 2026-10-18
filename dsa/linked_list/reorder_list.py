class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: ListNode | None) -> None:
        if head is None or head.next is None:
            return

        middle = self.middle(head)
        second_half = self.reverse(middle.next)
        middle.next = None

        first_half = head
        while second_half is not None:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next


def create_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(linked_list_to_list(head))
