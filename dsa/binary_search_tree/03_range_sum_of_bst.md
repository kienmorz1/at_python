# 03 — Range Sum of BST (LeetCode 938)

**Link:** https://leetcode.com/problems/range-sum-of-bst/

## Problem
Given the root of a BST and `low`, `high`, return the sum of values of all nodes with `low <= value <= high`.

Example: `root = [10,5,15,3,7,null,18]`, `low = 7`, `high = 15` → `32` (7 + 10 + 15).

## Approach
Recursion with **pruning** using BST order:
- `root.val < low` → root and its entire left subtree are too small. Skip them, recurse **right** only.
- `root.val > high` → root and its entire right subtree are too large. Skip them, recurse **left** only.
- Otherwise root is in range → add it, and recurse into **both** children (either side may contain more in-range values).

## Pattern to remember
> **Range query on BST = prune by comparing with low/high.** Only the subtrees that can overlap the range are visited.

## Complexity
- Time: O(n) worst case (range covers everything), but typically much less due to pruning.
- Space: O(h) recursion stack.

## Dry run
`root = [10,5,15,3,7,null,18]`, `low = 7`, `high = 15`

```
        10
       /  \
      5    15
     / \     \
    3   7    18
```

| Call | node | Check | Action | Returns |
|------|------|-------|--------|---------|
| 1 | 10 | 7 ≤ 10 ≤ 15 | 10 + left + right | |
| 2 | 5 (left of 10) | 5 < 7 | go right only → 7 | |
| 3 | 7 | in range | 7 + left(None→0) + right(None→0) | 7 |
| 4 | 15 (right of 10) | in range | 15 + left(None) + right(18) | |
| 5 | 18 | 18 > 15 | go left only → None → 0 | 0 |
| — | | | | 15 |

Total from 2-3: 7. From 4-5: 15. Root: 10. Sum = 10 + 7 + 15 = **32**.

Node `3` (left child of 5) and node `5` itself are never counted: since 5 < 7, the whole left side of 10 is pruned down to just the right path of 5, and 3 is never visited.

## Common mistakes
- Adding nodes outside the range (forgetting the `root.val < low` / `> high` checks).
- Returning early when root is out of range without recursing into the side that can still contain values.

## Full program (`03_range_sum_of_bst.py`)

```python
"""LeetCode 938 - Range Sum of BST (recursive solution).

Return the sum of all node values v such that low <= v <= high.
"""
from tree_utils import build_tree


class Solution:
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return (
            root.val +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([10, 5, 15, 3, 7, None, 18])
    print(sol.rangeSumBST(root, 7, 15))  # 32
    print(sol.rangeSumBST(root, 6, 10))  # 17
    assert sol.rangeSumBST(root, 7, 15) == 32
    assert sol.rangeSumBST(root, 6, 10) == 17
    print("all checks passed")
```
