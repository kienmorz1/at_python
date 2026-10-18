# Find the Length of a Linked-List Cycle

This program returns the number of nodes in a cycle, or zero if the list has
no cycle.

## Approach: detect a meeting, then count one lap

1. Run Floyd's slow/fast-pointer traversal. If the fast pointer reaches the
   end, return zero.
2. When the pointers meet, keep one pointer at the meeting node.
3. Start another pointer at the next node and count links until it returns
   to the meeting node.
4. Return the number of nodes counted in that lap.

It is not necessary to find the cycle's entry to measure its length. Starting
at any node in a cycle and following links once visits every cycle node
exactly once before returning to the start.

## Example walkthrough

For `1 -> 2 -> 3 -> 4 -> 2 ...`, the cycle consists of the nodes `2`, `3`,
and `4`. Once Floyd's pointers meet in the cycle, the counting walk makes
three moves around it and returns `3`.

## Complexity

- **Time:** O(n) overall; the cycle traversal counts at most one cycle lap
  after detection.
- **Extra space:** O(1).

The method does not mutate the list. A finite acyclic list and an empty list
both produce zero.
