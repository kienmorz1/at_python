# Find the Middle Node (First Middle for Even Length)

This version of the middle-node routine is the helper used by the reorder
program. It returns the sole middle node for odd-length lists and the first
of the two middle nodes for even-length lists.

## Approach: stop the fast pointer before its final two-node move

1. Initialize `slow` and `fast` at the head.
2. Advance `slow` once and `fast` twice only while both `fast.next` and
   `fast.next.next` exist.
3. When that condition is false, return `slow`.

The loop condition deliberately differs from the common condition
`fast is not None and fast.next is not None`. The latter returns the second
middle for an even-length list; this version stops at the first middle.

## Example

For `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the returned node contains `3`, the first
middle. For `1 -> 2 -> 3 -> 4 -> 5`, it contains `3`, the only middle.
An empty list returns `None`.

## Complexity

- **Time:** O(n).
- **Extra space:** O(1).

Only references are used; the list is not modified.
