# Basic Linked-List Operations

This program defines a singly linked list and demonstrates adding, removing,
printing, and counting nodes. Each node stores a `data` value and a `next`
reference; the list stores a `head` reference to its first node.

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
   node through its `next` reference.
7. **Remove from the end.** `removeLast` walks to the node immediately before
   the last one, saves the last value, disconnects the last node, and returns
   the saved value.

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
(`13`, `12`), and prints the remaining list:

```text
6 -> 5 -> 10 -> 11
```

## Complexity

Let `n` be the number of nodes.

| Operation | Time | Extra space |
|---|---:|---:|
| `printLL`, `size` | O(n) | O(1) |
| `addFirst`, `removeFirst` | O(1) | O(1) |
| `addLast`, `removeLast` | O(n) | O(1) |

## Current implementation edge cases

- `addLast` does not stop after calling `addFirst` on an empty list. It then
  creates and appends another node with the same value. Thus, appending to an
  empty list currently creates two nodes instead of one.
- `removeLast` handles an empty list, but its traversal assumes there are at
  least two nodes. Calling it on a one-node list raises an error when it tries
  to access `temp.next.next`.

These notes describe the current code; those edge cases are not exercised by
the sample sequence.
