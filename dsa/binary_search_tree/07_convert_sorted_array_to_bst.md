# 07 — Convert Sorted Array to BST (LeetCode 108)

**Link:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

## Problem
Given an array `nums` sorted in strictly increasing order, build a **height-balanced** BST (depth of the two subtrees of every node differs by at most 1).

Example: `nums = [-10,-3,0,5,9]` → one valid answer is `[0,-10,5,null,-3,null,9]`.

## Approach
Divide and conquer, the same idea as binary search:
- The **middle element** becomes the root. Everything to its left in the array is smaller, everything to the right is larger, so ordering holds.
- Left half of the array → build the left subtree. Right half → build the right subtree.
- Choosing the middle at every level keeps the two halves almost equal in size, which gives balance.

Inorder traversal of the result gives back the original array, which is a good self-check.

## Pattern to remember
> **Sorted array → BST = pick middle as root, recurse on each half.** Middle = balance.

## Complexity
- Time: O(n) — each element becomes exactly one node.
- Space: O(log n) recursion depth (balanced tree), plus O(n) for the output tree itself.

## Dry run
`nums = [-10,-3,0,5,9]`, indices 0..4

| Call | lo | hi | mid | nums[mid] | Node | Left range | Right range |
|------|----|----|-----|-----------|------|-----------|-------------|
| 1 | 0 | 4 | 2 | 0 | root 0 | build(0,1) | build(3,4) |
| 2 | 0 | 1 | 0 | -10 | left of 0 | build(0,-1)=None | build(1,1) |
| 3 | 1 | 1 | 1 | -3 | right of -10 | None | None |
| 4 | 3 | 4 | 3 | 5 | right of 0 | build(3,2)=None | build(4,4) |
| 5 | 4 | 4 | 4 | 9 | right of 5 | None | None |

Resulting tree:
```
        0
      /   \
   -10     5
     \       \
     -3       9
```
`to_list` = `[0, -10, 5, None, -3, None, 9]`. Height = 3, so it is balanced.

## Common mistakes
- Using `(lo + hi) / 2` in Python — returns a float. Use `//`.
- Off-by-one: recursing with `build(lo, mid)` instead of `build(lo, mid - 1)` causes infinite recursion.
- Choosing the first element as root → skewed tree (valid BST, but not balanced).

## Full program (`07_convert_sorted_array_to_bst.py`)

```python
"""LeetCode 108 - Convert Sorted Array to Binary Search Tree (recursive solution).

Given an integer array sorted in ascending order, build a height-balanced BST.
"""
from tree_utils import TreeNode, inorder, to_list


class Solution:
    def sortedArrayToBST(self, nums):

        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)


def _height(root):
    if not root:
        return 0
    return 1 + max(_height(root.left), _height(root.right))


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = sol.sortedArrayToBST(nums)
    print(to_list(root))  # [0, -10, 5, None, -3, None, 9]
    print(inorder(root))  # [-10, -3, 0, 5, 9]
    assert inorder(root) == nums
    assert _height(root) == 3  # balanced

    assert sol.sortedArrayToBST([]) is None
    assert sol.sortedArrayToBST([1]).val == 1
    print("all checks passed")
```
