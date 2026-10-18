class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def lengthOfLoop(self, head: ListNode | None) -> int:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                count = 1
                current = slow.next
                while current is not slow:
                    current = current.next
                    count += 1
                return count

        return 0


if __name__ == "__main__":
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second

    print(Solution().lengthOfLoop(first))
