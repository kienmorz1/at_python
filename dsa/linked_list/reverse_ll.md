# Reverse a Singly Linked List

This program reverses a linked list in place. Rather than creating new nodes,
it redirects each node's `next` reference so that it points to the previous
node.

## Approach: iterative pointer reversal

The method uses three pointers:

- `curr` is the node currently being processed.
- `prev` is the already-reversed prefix; it starts as `None`.
- `fwd` temporarily saves the next node so it remains reachable after the
  current link is changed.

For each node:

1. Save `curr.next` in `fwd`.
2. Point `curr.next` backward to `prev`.
3. Move `prev` to `curr`.
4. Move `curr` forward to the saved `fwd`.

When `curr` becomes `None`, every link has been reversed. `prev` is then the
new head and is returned.

## Example walkthrough

Starting with:

```text
1 -> 2 -> 3 -> 4 -> 5 -> None
```

The pointer changes build the reversed prefix one node at a time:

| Processed node | Reversed prefix (`prev`) | Unprocessed suffix (`curr`) |
|---:|---|---|
| — | `None` | `1 -> 2 -> 3 -> 4 -> 5` |
| 1 | `1 -> None` | `2 -> 3 -> 4 -> 5` |
| 2 | `2 -> 1 -> None` | `3 -> 4 -> 5` |
| 3 | `3 -> 2 -> 1 -> None` | `4 -> 5` |
| 4 | `4 -> 3 -> 2 -> 1 -> None` | `5` |
| 5 | `5 -> 4 -> 3 -> 2 -> 1 -> None` | `None` |

The returned head is the node containing `5`.

## Complexity

- **Time:** O(n), because every node is visited once.
- **Extra space:** O(1), because the existing nodes are rewired in place.

An empty list is also handled: the loop does not run and the method returns
`None`.
