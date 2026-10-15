# Find the Intersection of Two Linked Lists

The program finds the node at which two singly linked lists physically join.
Intersection means that both lists point to the same node object, not merely
that they contain nodes with equal values.

## Approach

1. **Measure both lists.** `getSize` traverses each list and counts its nodes,
   producing lengths `s1` and `s2`.
2. **Align their remaining lengths.** If one list is longer, advance its head
   by the length difference. The two pointers now have the same number of
   nodes remaining before the end.
3. **Walk both pointers together.** Advance `headA` and `headB` one node at a
   time until they refer to the same object.
4. **Return the shared node.** If the lists intersect, the pointers meet at
   their first shared node. If they do not, both eventually become `None`,
   which is returned.

The comparison is `headA != headB`, so it compares node identity rather than
the values stored in the nodes.

## Example walkthrough

The example constructs these lists, sharing the same `common_tail` nodes:

```text
A: 4 -> 1 --+
             +-> 8 -> 4 -> 5
B: 5 -> 6 -> 1 --+
```

1. List A has 5 nodes and list B has 6, so B's pointer advances once.
2. Both pointers now have 5 nodes remaining.
3. They move forward together. The two nodes containing `1` are different
   objects, so they are not mistaken for the intersection.
4. Both pointers reach the shared node containing `8`; that node is returned.

## Complexity

For lists of lengths `m` and `n`, counting and pointer alignment take O(m + n)
time overall. The algorithm uses O(1) extra space.

## Assumptions

- The input lists are acyclic.
- A genuine intersection is represented by shared node references. Equal
  values alone do not constitute an intersection.
