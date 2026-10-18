# Find the Start of a Linked-List Cycle

This program returns the node where a cycle begins, or `None` if the list is
acyclic.

## Approach: Floyd's meeting point

1. Move `slow` by one link and `fast` by two links until they meet or `fast`
   reaches the end.
2. If the fast pointer reaches the end, return `None`.
3. After a meeting, reset a pointer to the head while leaving the other at
   the meeting node.
4. Move both pointers one node at a time. Their next meeting point is the
   cycle entry; return that node.

The final comparison uses object identity (`is`), because the goal is to find
the shared node, not merely a node with the same value.

## Example walkthrough

For `1 -> 2 -> 3 -> 4 -> 2 ...`, the cycle starts at the node containing `2`.
The slow and fast pointers first meet somewhere inside the cycle. Resetting
one pointer to node `1` and advancing both at equal speed brings them
together at the cycle's first node (the original node `2`).

## Complexity

- **Time:** O(n) for cycle detection and locating its entry.
- **Extra space:** O(1).

The algorithm does not alter the links. Duplicate values do not cause a false
match because nodes are compared by identity.
