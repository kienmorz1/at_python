# Merge Two Sorted Linked Lists

This program combines two ascending singly linked lists into one ascending
list. It reuses the input nodes rather than creating a new node for every
value.

## Approach: dummy head and moving tail

1. Create a dummy node and use `dt` as the tail of the output list. The dummy
   lets the algorithm append the first selected node without a special case.
2. While both input pointers refer to nodes, compare their values.
3. Attach the smaller node to `dt.next`, advance that input pointer, and move
   `dt` to the node just attached. Equal values are taken from the first list
   first.
4. When either input is exhausted, connect the remaining nodes from the other
   list to the output tail. That remainder is already sorted.
5. Return `dh.next`, skipping the temporary dummy node.

## Example walkthrough

For `1 -> 2 -> 4` and `1 -> 3 -> 4`, the comparisons attach `1` from the first
list, `1` from the second, then `2`, `3`, and `4`. Once the second input is
exhausted, the remaining `4` is attached as-is. The result is:

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4
```

## Complexity

For input lengths `m` and `n`, the method takes O(m + n) time and O(1) extra
space. The output chain reuses the original nodes.

## Assumptions and mutation

Both input lists must be sorted in ascending order and must not share nodes.
The method rewires the input nodes into the result; treat the original lists
as consumed after calling it. Empty lists are supported, including the case
where both inputs are empty.
