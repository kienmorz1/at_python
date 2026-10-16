# Basic Linked-List Operations

This program defines a singly linked list and demonstrates adding, removing,
printing, and counting nodes. Each node stores a `data` value and a `next`
reference; the list stores a `head` reference to its first node. The list
supports insertion at either end and removal from the beginning, end, by
1-based position, or by value.

## How to think about each method

The central linked-list rule is: **a node is reached through a reference**.
`head` refers to the first node; each node's `next` refers to the following
node. To walk the list, keep a temporary reference and repeatedly follow
`next`. To remove a node, change the reference that points to it so it skips
over that node.

### `Node.__init__(data)` — create one link in the chain

1. Save the supplied value in `self.data`.
2. Set `self.next` to `None`, because a new node is not connected to a
   successor yet.

**Memory cue:** A node starts as **value + empty link**.

### `LL.__init__()` — start an empty list

Set `self.head` to `None`. There is no first node yet, so there is no chain to
traverse.

**Memory cue:** **No first node means `head` is `None`.**

### `printLL()` — visit and print every node

1. Copy `self.head` into `temp`. Moving `temp` lets the method traverse without
   changing the list's actual head.
2. While `temp` is not `None`, print its value.
3. Advance with `temp = temp.next`.
4. Stop when `temp` reaches `None`, which means the end of the chain.

**Memory cue:** **Start → use → advance → stop at `None`.**

### `size()` — count every node

1. Start `temp` at `self.head` and the count `c` at zero.
2. For each node (`temp is not None`), increase `c` by one.
3. Advance `temp` to `temp.next`.
4. Return `c` after traversal ends.

The empty list naturally returns zero because the loop never starts.

**Memory cue:** **Count, then move; return the count at the end.**

### `addFirst(x)` — insert before the current head

1. Create `new_node` containing `x`.
2. Point `new_node.next` at the current `self.head`. This preserves the
   existing chain.
3. Move `self.head` to `new_node`, making it the first node.

The order matters: connect the new node to the old chain before replacing
`head`.

**Memory cue:** **New node points to old head; head points to new node.**

### `removeFirst()` — move the head forward

1. If `self.head` is `None`, return `None`; there is nothing to remove.
2. Save the first node's value so it can still be returned.
3. Set `self.head` to `self.head.next`. The old first node is no longer part
   of the list.
4. Return the saved value.

**Memory cue:** **Save value → advance head → return value.**

### `addLast(x)` — connect a node after the tail

1. If the list is empty, call `addFirst(x)`.
2. Create a new node containing `x`.
3. Start `temp` at the head and follow `next` until `temp.next` is `None`.
   At that point, `temp` is the tail.
4. Set `temp.next` to the new node.

**Memory cue:** **Walk until the next link is empty; attach there.**

**Current-code caution:** After calling `addFirst(x)` for an empty list, this
method continues instead of returning. It therefore creates and attaches a
second node with the same value in that case.

### `removeLast()` — stop at the node before the tail

1. If the list is empty or has only one node, return `None`.
2. Start `temp` at the head.
3. Continue while `temp.next.next` is not `None`. This positions `temp` on
   the node immediately before the tail.
4. Set `temp.next` to `None`, disconnecting the tail.

The loop checks two links ahead so it stops *before* reaching the last node.
As written, this method does not save or return the removed value.

**Memory cue:** **To remove the tail, find its predecessor and clear its link.**

**Current-code caution:** The one-node case returns without removing that
node. For two or more nodes, the tail is removed, but the method still returns
`None`.

### `removeKthNode(k)` — bypass the node at a 1-based position

1. If `k == 1`, save the head value and move `self.head` to the second node.
   Return the saved value.
2. Otherwise, start `traverse` at the head and set the position counter `c`
   to 1.
3. Move forward until `traverse` is at position `k - 1`, the node just before
   the target.
4. Save the target value from `traverse.next`.
5. Bypass the target with
   `traverse.next = traverse.next.next`.
6. Return the saved value.

The predecessor is needed because a singly linked node has no link back to
the node before it.

**Memory cue:** **Find the predecessor → save target → link around target.**

**Current-code caution:** `k` is 1-based, and this implementation assumes the
list is non-empty and `k` is valid. It does not validate zero, negative, or
out-of-range positions.

### `removeXval(X)` — search for and bypass the first matching node

1. If the list is empty, return `None`.
2. Check the head separately. If its value is `X`, save the value, advance
   `self.head` to the next node, and return the saved value.
3. Otherwise, start `temp` at the head and `prev` at `None`.
4. For each node, compare `temp.data` with `X`.
   - If they match, save the value and set `prev.next` to `temp.next`. This
     bypasses the matching node. Return the saved value.
   - If they do not match, move `prev` to `temp`, then move `temp` to
     `temp.next`.
5. If traversal reaches `None`, return `None`; no value matched.

`prev` is necessary because the matching node must be unlinked through the
previous node's `next` reference. The separate head case handles the one node
that has no predecessor.

**Memory cue:** **Check head; then carry previous and current; bypass on match.**
Only the first matching node is removed.

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
