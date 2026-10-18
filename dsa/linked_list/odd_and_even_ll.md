# Group Odd- and Even-Positioned Nodes

The program rearranges a singly linked list so that nodes originally at odd
positions come first, followed by nodes originally at even positions. The
positions are one-based; this is based on position, not on whether a node's
value is odd or even.

## Approach: build two chains

1. Create dummy heads and tail pointers for the odd-position and
   even-position chains.
2. Walk the original list once, keeping the next node before changing any
   links.
3. Use a one-based index to append each node to the corresponding chain.
4. Clear each node's old `next` link before appending. This prevents stale
   links from creating accidental cycles or leaving old order in the result.
5. Connect the odd chain's tail to the even chain's head and return the first
   real odd-position node.

## Example walkthrough

For `10 -> 20 -> 30 -> 40 -> 50`, nodes at positions 1, 3, and 5 form
`10 -> 30 -> 50`. Nodes at positions 2 and 4 form `20 -> 40`. Joining these
chains produces:

```text
10 -> 30 -> 50 -> 20 -> 40
```

Relative order within each group is preserved.

## Complexity

- **Time:** O(n), because each node is visited once.
- **Extra space:** O(1), excluding the two temporary dummy nodes.

The input nodes are rewired in place. Empty and one-node lists are supported.
