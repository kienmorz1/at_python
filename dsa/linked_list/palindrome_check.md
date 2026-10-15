# Check Whether a Linked List Is a Palindrome

The program checks whether the values in a singly linked list read the same
from left to right and right to left. It avoids copying all values into an
array by finding the midpoint and reversing part of the list in place.

## Approach

1. **Handle short lists.** An empty list or a list with one node is immediately
   a palindrome.
2. **Find the first middle node.** `getMid` uses slow and fast pointers. Its
   loop stops at the first middle for an even-length list.
3. **Separate the second half.** Save `mid_node.next` as `head_2`, then set
   `mid_node.next` to `None`.
4. **Reverse the second half.** `reverseLL` reverses the links starting at
   `head_2`.
5. **Compare corresponding values.** Start one pointer at the original head
   and one at the reversed second half. If any pair of values differs, return
   `False`; if all compared pairs match, return `True`.

The first half is as long as, or one node longer than, the second half. The
middle value in an odd-length list does not need to be compared with another
value.

## Example walkthrough: `[1, 2, 2, 1]`

1. `getMid` returns the first middle node, containing `2`.
2. The list is split into `1 -> 2` and `2 -> 1`.
3. Reversing the second half produces `1 -> 2`.
4. Compare the first half (`1 -> 2`) with the reversed half (`1 -> 2`).
   Every pair matches, so the method returns `True`.

For `[1, 2]`, the two compared values are `1` and `2`, so the method returns
`False`.

## Complexity

- **Time:** O(n) to find the midpoint, reverse the second half, and compare.
- **Extra space:** O(1); the list links are rearranged in place.

## Current implementation note

The method mutates the input list: it splits the list and reverses its second
half, and it does not restore the original links before returning. On a
mismatch, it returns early with the list still modified as well. Callers that
need to keep the original list structure should account for this behavior.
