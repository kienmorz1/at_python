# Reference: Binary Tree Concepts and Terminology

This document describes the structure, components, and primary terms of a binary tree.

---

## 1. Technical Definition

A **binary tree** is a non-linear, hierarchical data structure. 
It consists of elements called **nodes** connected by directed links called **edges**.

### Core Constraint
Every node in a binary tree has **at most two children**, referred to as the **left child** and the **right child**.

```text
               [ Root Node ]
               /           \
     [ Left Child ]     [ Right Child ]
```

---

## 2. Anatomy and Key Terminology

```text
                 Level 0  ----->         ( A )               <-- Root
                                        /     \
                 Level 1  ----->      ( B )   ( C )          <-- Ancestors of D, E, F
                                     /    \       \
                 Level 2  ----->   ( D )  ( E )   ( F )      <-- Leaves / Siblings (D, E)
```

| Term | Definition | Example in Diagram Above |
| :--- | :--- | :--- |
| **Node** | A fundamental data container holding a value and pointers to child nodes. | Any circle: `A`, `B`, `C`, etc. |
| **Root** | The topmost node of the tree. It has no parent. | Node `A` |
| **Edge** | The link or reference connecting a parent node to a child node. | The line between `A` and `B` |
| **Parent** | A node that contains a reference to subordinate child nodes. | Node `B` is parent to `D` and `E` |
| **Child** | A node directly connected below another node. | Node `D` is a left child of `B` |
| **Siblings** | Nodes that share the exact same parent node. | `(D, E)` are siblings |
| **Leaf (External Node)** | A node that has zero children (`left is None` and `right is None`). | Nodes `D`, `E`, and `F` |
| **Internal Node** | A node that has at least one non-null child. | Nodes `A`, `B`, and `C` |
| **Subtree** | Any node treated as the root of its own smaller binary tree. | Node `B` with children `(D, E)` |
| **Depth of a Node** | The number of edges from the root node down to that specific node. | Depth of `D` is `2` |
| **Height of a Node** | The number of edges on the longest downward path from that node to a leaf. | Height of `B` is `1` |
| **Height of the Tree** | The height of the root node (longest path from root to any leaf). | Height is `2` |

---

## 3. Standard Binary Tree Class Representation

In Python, a tree node is represented as an object with three fields:
1. `data`: The value stored inside the node.
2. `left`: Pointer/reference to the left subtree (or `None`).
3. `right`: Pointer/reference to the right subtree (or `None`).

```python
class TreeNode:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None
```

---

## 4. Common Structural Variations

| Tree Variant | Structural Rule | Visual Example |
| :--- | :--- | :--- |
| **Full Binary Tree** | Every node has either **0 or 2** children. No node has only 1 child. | `(A) -> left:(B), right:(C)` |
| **Complete Binary Tree** | All levels are filled completely except possibly the last level, which fills **from left to right**. | Used in Binary Heaps |
| **Perfect Binary Tree** | All internal nodes have 2 children, and all leaf nodes sit at the exact same depth. | Complete symmetry |
| **Skewed Binary Tree** | Every parent node has only one child branch (behaves like a Linked List). | All-left or all-right chain |

---

## 5. Technical Justification: Why Trees Over Linear Lists?

- **Hierarchical Representation:** Naturally models folder directories, parse trees in compilers, and DOM structures in browsers.
- **Efficient Searching (when ordered as BST):** Provides average-case $\mathcal{O}(\log N)$ lookups, insertions, and deletions compared to $\mathcal{O}(N)$ in unsorted arrays or linked lists.
- **Recursive Symmetry:** Every subtree is itself a binary tree, enabling simple divide-and-conquer implementations for traversal and measurement.