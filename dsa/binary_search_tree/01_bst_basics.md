# Binary Search Tree (BST) — Basics

## What is a BST?

A **Binary Search Tree** is a binary tree (every node has at most 2 children) where the nodes are arranged so that searching can discard half the tree at every step.

## Properties

For **every** node `N` in the tree:

1. All values in `N.left` subtree are **strictly less** than `N.val`.
2. All values in `N.right` subtree are **strictly greater** than `N.val`.
3. Both left and right subtrees are themselves BSTs.
4. (Usually) no duplicate values. LeetCode problems that allow duplicates say so explicitly.

Key consequence:

- **In-order traversal (left → node → right) of a BST gives a sorted sequence.** This is the single most useful fact for BST problems.

## Operations and complexity

| Operation | Average (balanced) | Worst (skewed) |
|-----------|--------------------|----------------|
| Search    | O(log n)           | O(n)           |
| Insert    | O(log n)           | O(n)           |
| Delete    | O(log n)           | O(n)           |
| Min / Max | O(log n)           | O(n)           |

Worst case happens when the tree degenerates into a linked list (e.g. inserting 1, 2, 3, 4, 5 in order).

## How to identify a BST

### Quick check (WRONG, but common)
"Left child < parent < right child" for each parent-child pair. **This is not enough.**

Counter-example:
```
      5
     / \
    1   4
       / \
      3   6
```
Here 4 is the right child of 5 but 4 < 5, so the very first parent-child check already fails. Take a subtler example, where every parent-child pair is fine:
```
      10
     /  \
    5    15
        /  \
       6    20
```
`6` is a left child of `15` (6 < 15 ✓), and `15` is right child of `10` (15 > 10 ✓). But `6` sits in the right subtree of `10`, so it must be `> 10`. It is `< 10`, so this is **not** a BST.

### Correct check
Every node must lie within a **range (low, high)** inherited from its ancestors:

- Root starts with `(-inf, +inf)`.
- Going left: the upper bound becomes `node.val`.
- Going right: the lower bound becomes `node.val`.
- A node is valid only if `low < node.val < high`.

Alternative: do an in-order traversal and check the sequence is strictly increasing.

## Pattern cheat sheet

| Problem type | Pattern |
|--------------|---------|
| Search / find a value | Walk left or right based on comparison (O(h)) |
| Count / sum in a range | Prune subtrees using `val < low` / `val > high` |
| Validate BST | Pass `(low, high)` bounds down, or in-order check |
| Insert | Walk down like search, attach a new leaf where it falls off |
| Delete | Find node; 0/1 child → splice out; 2 children → replace with in-order successor |
| Build from sorted array | Pick middle as root, recurse on both halves (balanced) |
| Lowest common ancestor | First node where p and q split (or one equals node) |

## Traversal reminder

- In-order (L, N, R) → sorted output for a BST.
- Pre-order (N, L, R) → good for copying/serialising.
- Post-order (L, R, N) → good for deleting or computing heights.
- Level-order (BFS) → good for "by level" problems.

## Related files in this folder

- `tree_utils.py` — `TreeNode`, `build_tree` (LeetCode level-order format), `to_list`, `inorder`.
- `01_search_in_bst.py` … `07_convert_sorted_array_to_bst.py` — solutions. Each has a matching `.md` write-up.
