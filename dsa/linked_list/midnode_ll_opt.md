# Find the Middle Node

This program finds and returns the middle node of a singly linked list using
two pointers that move at different speeds.

## Approach: slow and fast pointers

1. Initialize both `slow` and `fast` to the head.
2. Continue while `fast` and `fast.next` both exist.
3. Move `slow` forward by one node and `fast` forward by two nodes.
4. When `fast` reaches the end (or cannot make another two-node move),
   `slow` is at the middle.
5. Return `slow`. The returned value is a node reference, so printing from it
   shows the suffix beginning at the middle, not just the middle value.

Because the fast pointer moves twice as quickly, it reaches the end after the
slow pointer has covered about half the list.

## Which middle is returned?

- For an odd-length list, the single middle node is returned.
- For an even-length list, this implementation returns the **second** of the
  two middle nodes. For example, in `1 -> 2 -> 3 -> 4 -> 5 -> 6`, it returns
  the node containing `4`.
- An empty list returns `None`.

## Example walkthrough

For `1 -> 2 -> 3 -> 4 -> 5`:

| Iteration | `slow` | `fast` |
|---|---:|---:|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

The loop then stops because `fast.next` is `None`. The method returns the node
containing `3`.

For `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the pointers make three moves; `slow` ends
at `4`, so this is the second middle.

## Complexity

- **Time:** O(n), because the fast pointer traverses the list once.
- **Extra space:** O(1), because only two pointers are used.
