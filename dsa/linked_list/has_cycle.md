# Check Whether a Linked List Has a Cycle

This program returns whether following `next` references eventually revisits
a node.

## Approach: Floyd's slow and fast pointers

1. Start both pointers at the head.
2. Move `slow` by one node and `fast` by two nodes while `fast` and
   `fast.next` exist.
3. If the pointers refer to the same node, a cycle exists.
4. If `fast` reaches `None` or cannot advance, the list terminates and has no
   cycle.

The comparison is by node identity, not node value. In a cycle, the fast
pointer gains one node per iteration on the slow pointer, so it must
eventually meet it.

## Example

```text
1 -> 2 -> 3 -> 4
     ^         |
     +---------+
```

The pointers eventually meet within the loop, so the method returns `True`.
For a normal terminating list, `fast` reaches the end and it returns `False`.

## Complexity

- **Time:** O(n) before termination or pointer meeting.
- **Extra space:** O(1).

The list is not modified. An empty list and a one-node list without a
self-reference both return `False`.
