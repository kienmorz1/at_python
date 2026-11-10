# Subsets II (With Duplicates)

**File:** `subset_2.py`
**Topic:** Backtracking — pick / not pick, with duplicate skipping
**Difficulty:** Medium
**Also known as:** LeetCode 90

---

## 1. Problem

You get a list of integers `nums`. The list can contain duplicates. Return all possible subsets. The answer must not contain duplicate subsets.

## 2. Examples

| Input | Output |
|-------|--------|
| `[1, 2, 2]` | `[[1,2,2],[1,2],[1],[2,2],[2],[]]` |
| `[0]` | `[[0],[]]` |

Actual output of the program (`[1, 2, 2, 3]`):

```text
[[1, 2, 2, 3], [1, 2, 2], [1, 2, 3], [1, 2], [1, 3], [1], [2, 2, 3], [2, 2], [2, 3], [2], [3], []]
```

There are 12 subsets, not 16. The method removes the 4 duplicates.

## 3. Key Idea (Shortcut)

> **Sort first. Duplicates are then next to each other.**
> **PICK: go to `index + 1`.**
> **DO NOT PICK: skip ALL copies of this value. Go to the next different value.**

Why this works: If you skip one `2`, you must skip all the `2`s at that point. If you keep one of the later `2`s, you make a subset that the "pick" branch already made.

## 4. Approach

1. Sort `nums`.
2. Call `ss(0, [])`.
3. In `ss(index, current_ans)`:
   1. If `index == len(nums)`, save a copy of `current_ans`. Then return.
   2. Append `nums[index]`. Call `ss(index + 1)`. (Pick)
   3. Pop the last element. (Undo)
   4. Set `next_index = index + 1`. Move `next_index` forward while `nums[next_index] == nums[index]`.
   5. Call `ss(next_index)`. (Do not pick any copy of this value)
4. Return `result`.

## 5. Code

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def ss(index, current_ans):
            if index == len(nums):
                result.append(list(current_ans))
                return
            current_ans.append(nums[index])       # pick
            ss(index + 1, current_ans)
            current_ans.pop()                     # undo
            next_index = index + 1                # skip all copies
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            ss(next_index, current_ans)           # do not pick

        ss(0, [])
        return result

sol = Solution()
print(sol.subsetsWithDup([1, 2, 2, 3]))
```

## 6. Recursion Tree ([1, 2, 2])

Left = pick (`index + 1`). Right = skip all copies (`next_index`).

```text
                            []  i=0 (1)
                 /                         \
            [1]  i=1 (2)                   []  i=1 (2)
           /           \                  /          \
    [1,2] i=2 (2)    [1]  i=3        [2] i=2 (2)    []  i=3
     /        \       SAVE           /       \       SAVE
 [1,2,2]    [1,2]                 [2,2]      [2]
  SAVE       SAVE                  SAVE      SAVE
```

The right branch at `i=1` jumps to `i=3`. It skips both `2`s. Thus, `[1,2]` and `[2]` occur only one time.

## 7. Complexity

| Measure | Value | Reason |
|---------|-------|--------|
| Time | O(n · 2^n) | Sorting is O(n log n). In the worst case (no duplicates), there are `2^n` subsets. Copying each costs O(n). |
| Space | O(n) | The recursion depth is `n` (not counting the output). |

## 8. Edge Cases

- All elements the same, `[2, 2, 2]`: The output is `[[2,2,2],[2,2],[2],[]]`. There are `n + 1` subsets.
- No duplicates: The method gives the same result as Subsets I.
- Empty list `[]`: The output is `[[]]`.

## 9. Common Mistakes

- Do not forget to sort. Without sorting, duplicates are not next to each other. The skip loop then fails.
- Do not skip duplicates in the "pick" branch. Skip them only in the "do not pick" branch.
- Do not use a `set` of tuples to remove duplicates. It works, but it is slow. Interviewers expect the skip method.

## 10. Interview Tips

- Say: "Sort, then skip duplicates in the not-pick branch."
- Compare with `subset_1.md`. The only new parts are `sort()` and the `while` loop.
- Show the other common form (loop-based). It uses the same idea:

  ```python
  def backtrack(start, path):
      result.append(path[:])
      for i in range(start, len(nums)):
          if i > start and nums[i] == nums[i - 1]:
              continue          # skip duplicate at the same level
          path.append(nums[i])
          backtrack(i + 1, path)
          path.pop()
  ```

- The rule `i > start and nums[i] == nums[i-1]` is also in Combination Sum II and Permutations II. Learn it one time and use it again.

## 11. Related Problems

- Subsets (LeetCode 78) — see `subset_1.md`
- Combination Sum II (LeetCode 40)
- Permutations II (LeetCode 47)
