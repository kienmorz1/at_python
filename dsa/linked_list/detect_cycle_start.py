class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break

        if fast is None or fast.next is None:
            return None

        from_head = head
        while from_head is not slow:
            from_head = from_head.next
            slow = slow.next

        return from_head


if __name__ == "__main__":
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    entry = Solution().detectCycle(first)
    print(entry.val if entry is not None else None)
