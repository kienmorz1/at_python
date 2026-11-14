# 04 — Validate Binary Search Tree (LeetCode 98)

**Link:** https://leetcode.com/problems/validate-binary-search-tree/

## Problem
Given `root`, return `True` if it is a valid BST, else `False`.

Examples:
- `[2,1,3]` → `True`
- `[5,1,4,null,null,3,6]` → `False` (4 is the right child of 5 but 4 < 5; also 3 is in 5's right subtree but 3 < 5)

## Approach 1 — Top-down with bounds (alternative)
The trap is checking only `left.val < node.val < right.val` for each node. That misses ancestors further up. Instead, every node must satisfy a **range** inherited from *all* its ancestors:

- Start with `(-inf, +inf)` at the root.
- Moving to the left child: new upper bound = `node.val` (lower bound unchanged).
- Moving to the right child: new lower bound = `node.val` (upper bound unchanged).
- A node is valid only if `low < node.val < high`.

Alternative (also correct): in-order traversal must produce a strictly increasing list.

## Approach 2 — Bottom-up with a summary per subtree (submitted solution)
Each call returns a summary object for its subtree: `minTree`, `maxTree`, and `isBST`.
- An empty subtree returns min = +10^13, max = -10^13, isBST = True. These sentinels are neutral in the comparisons below.
- For a node, the subtree is valid when both children are valid, `lans.maxTree < node.val`, and `rans.minTree > node.val`.
- The node's own min and max are the min and max over the node and both children.

```python
class dataObj:
    def __init__(self):
        self.minTree = 10 ** 13
        self.maxTree = -10 ** 13
        self.isBST = True

def isValidBST(self, root):
    def helper(node):
        if node is None:
            return self.dataObj()
        lans = helper(node.left)
        rans = helper(node.right)
        c1 = lans.isBST
        c2 = rans.isBST
        c3 = lans.maxTree < node.val
        c4 = rans.minTree > node.val
        myans = self.dataObj()
        myans.maxTree = max(node.val, lans.maxTree, rans.maxTree)
        myans.minTree = min(node.val, lans.minTree, rans.minTree)
        myans.isBST = c1 and c2 and c3 and c4
        return myans
    return helper(root).isBST
```

Dry run for `root = [5,1,4,null,null,3,6]`:
- Node 1: leaf, isBST = True, min = max = 1.
- Node 3 (under 4): leaf, min = max = 3.
- Node 6 (under 4): leaf, min = max = 6.
- Node 4: lans.max 3 < 4 ✓, rans.min 6 > 4 ✓ → valid. Its summary is min 3, max 6.
- Node 5: lans.max 1 < 5 ✓, but rans.min = 3 > 5 ✗ → isBST = False. The summary for the root says False.

The mistake is caught at the root, because the minimum of the right subtree (3) is smaller than 5.

Both approaches check the same rule. Approach 1 passes bounds down, and Approach 2 passes summaries up. Approach 2 can be a little heavier because it builds an object per node.

## Pattern to remember
> **Validate BST = carry `(low, high)` down the recursion (Approach 1), or return `(min, max, isBST)` up the recursion (Approach 2).** Both are O(n).

## Complexity
- Time: O(n) — every node visited once.
- Space: O(h) recursion stack.

## Dry run
`root = [5,1,4,null,null,3,6]`

```
      5
     / \
    1   4
       / \
      3   6
```

| Call | node | range (low, high) | Check | Result |
|------|------|-------------------|-------|--------|
| 1 | 5 | (-inf, inf) | ok | recurse left & right |
| 2 | 1 (left of 5) | (-inf, 5) | 1 in range | ok |
| 3 | 4 (right of 5) | (5, inf) | 4 > 5? **No** | return False |

Returns `False` immediately. The check at node 4 fails because it is in the right subtree of 5, so it must be greater than 5.

## Common mistakes
- Using `root.left.val < root.val < root.right.val` only (local check).
- Using `int` min/max for bounds — fails when node values equal `-2**31`. Use `float('-inf')` / `float('inf')`.
- Allowing equal values (`<=`) when the problem requires strictly less/greater.

## Full program (`04_validate_binary_search_tree.py`)

```python
"""LeetCode 98 - Validate Binary Search Tree (recursive solution, bottom-up).

Each call returns a summary (min, max, isBST) of its subtree. A node is a valid BST root
when both children are valid, the left max is < node.val and the right min is > node.val.
"""
from tree_utils import build_tree


class Solution:
    class dataObj:
        def __init__(self):
            self.minTree = 10 ** 13
            self.maxTree = -10 ** 13
            self.isBST = True

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node):
            if node is None:
                return self.dataObj()

            lans = helper(node.left)
            rans = helper(node.right)

            c1 = lans.isBST
            c2 = rans.isBST
            c3 = lans.maxTree < node.val
            c4 = rans.minTree > node.val

            myans = self.dataObj()
            myans.maxTree = max(node.val, lans.maxTree, rans.maxTree)
            myans.minTree = min(node.val, lans.minTree, rans.minTree)
            myans.isBST = c1 and c2 and c3 and c4

            return myans
        return helper(root).isBST


if __name__ == "__main__":
    sol = Solution()
    good = build_tree([2, 1, 3])
    bad = build_tree([5, 1, 4, None, None, 3, 6])  # 4 and 3 sit wrongly under 5
    print(sol.isValidBST(good))  # True
    print(sol.isValidBST(bad))   # False
    assert sol.isValidBST(good) is True
    assert sol.isValidBST(bad) is False
    print("all checks passed")
```
