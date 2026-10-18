class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        odd_dummy = ListNode()
        odd_tail = odd_dummy
        even_dummy = ListNode()
        even_tail = even_dummy

        index = 1
        current = head

        while current is not None:
            next_node = current.next
            current.next = None

            if index % 2 == 1:
                odd_tail.next = current
                odd_tail = current
            else:
                even_tail.next = current
                even_tail = current

            current = next_node
            index += 1

        odd_tail.next = even_dummy.next
        return odd_dummy.next


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
    result = Solution().oddEvenList(head)
    print(linked_list_to_list(result))
