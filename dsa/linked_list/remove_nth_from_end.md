# Remove the Nth Node from the End

This program removes the node `k` positions from the end of a singly linked
list and returns the possibly updated head.

## Approach: two pointers with a dummy node

1. Place a dummy node before the head. This gives the head a predecessor and
   lets the same unlinking operation remove either the first or an interior
   node.
2. Start `fast` and `slow` at the dummy node.
3. Advance `fast` by `k` nodes. This creates a gap of `k` between the
   pointers.
4. Move both pointers one node at a time until `fast` reaches the last node.
   `slow` is then immediately before the target node.
5. Bypass the target with `slow.next = slow.next.next`, then return the node
   after the dummy.

The implementation leaves the list unchanged for `k <= 0` or `k` greater
than the list length. For valid `k`, the target is removed in one traversal.

## Example walkthrough

For `1 -> 2 -> 3 -> 4 -> 5` with `k = 2`, `fast` first moves to node 2.
Then both pointers advance until `fast` is at node 5 and `slow` is at node 3.
The link from node 3 skips node 4, producing:

```text
1 -> 2 -> 3 -> 5
```

## Complexity

- **Time:** O(n), with one forward traversal.
- **Extra space:** O(1).

The list is modified in place. When `k` equals the list length, the head is
removed and the returned head is the former second node.
