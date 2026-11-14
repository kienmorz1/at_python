"""Shared helpers for the BST practice files.

- TreeNode: same class LeetCode uses.
- build_tree: builds a tree from LeetCode's level-order list, e.g. [4, 2, 7, 1, 3, None, None].
- to_list: converts a tree back into LeetCode's level-order list (trailing None trimmed).
- inorder: returns the in-order values (sorted for a valid BST).
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_list(root):
    if not root:
        return []
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
