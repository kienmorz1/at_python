# Reorder a Linked List

This program rearranges nodes in place from
`L0 -> L1 -> ... -> Ln` into
`L0 -> Ln -> L1 -> Ln-1 -> ...`. It changes links rather than copying values
or allocating replacement list nodes.

## Approach: split, reverse, and weave

1. **Find the first middle.** The `middle` helper stops at the first middle
   when the list length is even. This keeps the first half as long as, or one
   node longer than, the second half.
2. **Split the list.** Save `middle.next` as the second half and terminate the
   first half by setting `middle.next` to `None`.
3. **Reverse the second half.** The iterative `reverse` helper flips its
   links, so the farthest original node becomes the next node to weave in.
4. **Alternate nodes.** Save the next node from each half before updating
   links, then insert one node from the reversed half after one node from the
   first half. Continue until the second half is exhausted.

The save-before-rewire step ensures neither remaining part of the list is
lost when links are changed.

## Example walkthrough

For `1 -> 2 -> 3 -> 4 -> 5`, the first middle is `3`. The split is
`1 -> 2 -> 3` and `4 -> 5`; reversing the second half gives `5 -> 4`.
Alternating the nodes produces:

```text
1 -> 5 -> 2 -> 4 -> 3
```

The method follows the in-place API convention and returns `None`; inspect
the original `head` reference after the call to see the reordered chain.

## Complexity

- **Time:** O(n) to find the middle, reverse the second half, and weave.
- **Extra space:** O(1).

Empty and one-node lists are left unchanged. The operation mutates the input
list.
