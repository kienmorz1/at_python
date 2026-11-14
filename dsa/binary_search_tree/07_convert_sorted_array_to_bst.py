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
