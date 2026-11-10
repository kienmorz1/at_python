# Subsets (Power Set)

**File:** `subset_1.py`
**Topic:** Backtracking — pick / not pick
**Difficulty:** Medium
**Also known as:** LeetCode 78

---

## 1. Problem

You get a list of unique integers `nums`. Return all possible subsets (the power set). The answer must not contain duplicate subsets.

## 2. Examples

| Input | Output |
|-------|--------|
| `[1, 2, 3]` | `[[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]` |
| `[0]` | `[[0],[]]` |

Expected output of the program (after the fix in Section 3):

```text
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
```

## 3. Bug in the Current File

**WARNING:** The current file prints `None`. The function `subsets` does not return `result`.

To correct the bug, add this line at the end of `subsets`, after `ss(0, [])`:

```python
        return result
```

## 4. Key Idea (Shortcut)

> **For each element, make two choices: PICK it or DO NOT PICK it.**
> **n elements → 2^n subsets.**

Each level of the tree is one element. The left branch picks the element. The right branch skips it.

## 5. Approach

1. Make an empty `result` list.
2. Call `ss(0, [])`.
3. In `ss(index, current_ans)`:
   1. If `index == len(nums)`, save a **copy** of `current_ans`. Then return.
   2. Append `nums[index]`. Call `ss(index + 1)`. (Pick)
   3. Pop the last element. (Undo)
   4. Call `ss(index + 1)` again. (Do not pick)
4. Return `result`.

## 6. Code (Corrected)

```python
class Solution(object):
    def subsets(self, nums):
        result = []

        def ss(index, current_ans):
            if index == len(nums):
                result.append(list(current_ans))   # save a copy
                return
            current_ans.append(nums[index])         # pick
            ss(index + 1, current_ans)
            current_ans.pop()                       # undo
            ss(index + 1, current_ans)              # do not pick

        ss(0, [])
        return result

sol = Solution()
print(sol.subsets([1, 2, 3]))
```

## 7. Recursion Tree ([1, 2, 3])

Left = pick. Right = do not pick.

```text
                        []
               /                 \
            [1]                   []              (element 1)
          /     \               /     \
      [1,2]     [1]           [2]      []         (element 2)
      /   \     /  \         /   \    /  \
 [1,2,3] [1,2] [1,3] [1]  [2,3] [2] [3]  []       (element 3)
```

The leaves are the 8 subsets. The order of the leaves is the order of the output.

## 8. Complexity

| Measure | Value | Reason |
|---------|-------|--------|
| Time | O(n · 2^n) | There are `2^n` subsets. Copying each subset costs up to O(n). |
| Space | O(n) | The recursion depth is `n` (not counting the output). |

## 9. Edge Cases

- Empty list `[]`: The output is `[[]]`. The empty set is always a subset.
- One element `[x]`: The output is `[[x], []]`.

## 10. Common Mistakes

- Do not use `result.append(current_ans)`. All entries then point to the same list. At the end, that list is empty. Use `list(current_ans)` or `current_ans[:]`.
- Do not forget `pop()`. Without it, the "do not pick" branch still contains the element.
- Do not forget `return result`. This is the bug in the current file.

## 11. Interview Tips

- Draw the pick / not-pick tree first. Then write the code.
- Mention two other methods:
  - **Loop method:** Start with `[[]]`. For each number, add it to a copy of each old subset.

    ```python
    res = [[]]
    for x in nums:
        res += [s + [x] for s in res]
    ```

  - **Bitmask method:** Each number from `0` to `2^n - 1` is one subset. Bit `i` set means "pick `nums[i]`."
- If the input can have duplicates, see `subset_2.md`.

## 12. Related Problems

- Subsets II (LeetCode 90) — see `subset_2.md`
- Combination Sum (LeetCode 39)
- Combinations (LeetCode 77)
