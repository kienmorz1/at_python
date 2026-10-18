class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, k: int) -> ListNode | None:
        if k <= 0:
            return head

        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy

        for _ in range(k):
            fast = fast.next
            if fast is None:
                return head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


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
    result = Solution().removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))
