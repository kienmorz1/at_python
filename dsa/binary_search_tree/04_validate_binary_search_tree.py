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
