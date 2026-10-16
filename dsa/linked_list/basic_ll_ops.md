# Basic Linked-List Operations

This program defines a singly linked list and demonstrates adding, removing,
printing, and counting nodes. Each node stores a `data` value and a `next`
reference; the list stores a `head` reference to its first node. The list
supports insertion at either end and removal from the beginning, end, by
1-based position, or by value.

## Approach

1. **Represent each element as a node.** `Node` stores the element in `data`
   and initializes `next` to `None`.
2. **Keep track of the first node.** `LL.head` is `None` for an empty list and
   points to the first node otherwise.
3. **Traverse by following links.** Methods such as `printLL` and `size` begin
   at `head`, process the current node, then advance using `temp.next` until
   reaching `None`.
4. **Insert at the beginning.** `addFirst` creates a node, points it at the
   old head, and updates `head`. This takes constant time.
5. **Remove from the beginning.** `removeFirst` saves the head's value, moves
   `head` to the next node, and returns the saved value. It returns `None` if
   the list is empty.
6. **Insert at the end.** `addLast` walks to the last node and connects a new
   node through its `next` reference. If the list is empty, it calls
   `addFirst`.
7. **Remove from the end.** `removeLast` walks to the node immediately before
   the last one and disconnects the last node. It currently returns `None`
   whether or not a node was removed.
8. **Remove by position.** `removeKthNode(k)` treats `k` as a 1-based position,
   unlinks that node, and returns its value. For example, `k == 1` removes the
   head.
9. **Remove by value.** `removeXval(X)` searches from the head, unlinks the
   first node whose value equals `X`, and returns that value. It returns
   `None` if the list is empty or no matching value is found.
10. **Count and print.** `size` traverses the list and returns its number of
    nodes. `printLL` prints each node's value on its own line.

## Example walkthrough

The script first calls `addFirst` with `5`, `6`, `7`, `8`, and `9`. Since each
new node becomes the head, the list is:

```text
9 -> 8 -> 7 -> 6 -> 5
```

It removes and prints the first three values (`9`, `8`, `7`), leaving:

```text
6 -> 5
```

It then appends `10`, `11`, `12`, and `13`, removes the last two values
(`13`, `12`), and prints the remaining list. `removeLast` returns `None`, so
the two demonstration messages show `None` even though the tail nodes are
removed:

```text
6 -> 5 -> 10 -> 11
```

Next, `removeKthNode(2)` removes the value `5`, leaving `6 -> 10 -> 11`.
Finally, `removeXval(6)` finds and removes the head value `6`, leaving
`10 -> 11`.

## Complexity

Let `n` be the number of nodes.

| Operation | Time | Extra space |
|---|---:|---:|
| `printLL`, `size` | O(n) | O(1) |
| `addFirst`, `removeFirst` | O(1) | O(1) |
| `addLast`, `removeLast` | O(n) | O(1) |
| `removeKthNode(k)` | O(k) | O(1) |
| `removeXval(X)` | O(n) | O(1) |

## Current implementation edge cases

- `addLast` calls `addFirst` when the list is empty but does not return
  afterward. It then creates and appends another node with the same value, so
  appending to an empty list currently creates two nodes.
- `removeLast` returns `None` for an empty or one-node list. In the one-node
  case, it leaves the node in place. With two or more nodes, it removes the
  last node but still returns `None`.
- `removeKthNode` assumes the list is non-empty and `k` is a valid 1-based
  position. It does not validate `k`; a non-positive `k` may remove the wrong
  node, while an empty list or a position beyond the list can raise an error.

These notes describe the current code, including the edge cases above.
