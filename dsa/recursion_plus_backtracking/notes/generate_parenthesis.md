# Generate Parentheses

* **File:** `generate_parenthesis.py`
* **Topic:** Backtracking with constraints (pruning)
* **Difficulty:** Medium
* **Also known as:** LeetCode 22

---

## 1. Problem

You get an integer `n`. Make all strings of `n` pairs of parentheses that are well-formed (balanced).

## 2. Examples

| Input | Output |
|-------|--------|
| `n = 1` | `['()']` |
| `n = 2` | `['(())', '()()']` |
| `n = 3` | `['((()))', '(()())', '(())()', '()(())', '()()()']` |

Actual output of the program (`n = 2`):

```text
['(())', '()()']
```

## 3. Key Idea (Shortcut)

> **Add `(` if `open < n`.**
> **Add `)` if `close < open`.**
> **Save the string when `open == close == n`.**

These two rules keep the string valid at each step. Thus, you never make an invalid string. You do not need a separate validity check.

## 4. Approach

1. Start with an empty string, `open = 0`, and `close = 0`.
2. If `open` and `close` are both equal to `n`, add the string to the answer. Then return.
3. If `open < n`, add `(` and recurse with `open + 1`.
4. If `open > close`, add `)` and recurse with `close + 1`.

Note: The code makes a new string with `s + '('`. Thus, no "undo" step is necessary. The old string `s` does not change.

## 5. Code

```python
class Solution:
    def parentAdd(self, s, open_count, close, ans, n):
        if open_count == close == n:
            ans.append(s)
            return
        if open_count < n:
            self.parentAdd(s + '(', open_count + 1, close, ans, n)
        if open_count > close:
            self.parentAdd(s + ')', open_count, close + 1, ans, n)

    def generateParenthesis(self, n):
        ans = []
        self.parentAdd("", 0, 0, ans, n)
        return ans

sol = Solution()
print(sol.generateParenthesis(2))
```

## 6. Recursion Tree (n = 2)

Each node shows `string (open, close)`.

```text
                  "" (0,0)
                     |
                 "(" (1,0)
               /           \
        "((" (2,0)        "()" (1,1)
             |                 |
       "(()" (2,1)        "()(" (2,1)
             |                 |
      "(())" (2,2) SAVE   "()()" (2,2) SAVE
```

The tree never makes `")"` first. The rule `open > close` blocks it.

## 7. Complexity

| Measure | Value | Reason |
|---------|-------|--------|
| Time | O(4^n / √n) | The number of answers is the n-th Catalan number. Each answer has length `2n`. |
| Space | O(n) | The recursion depth is `2n` (not counting the output). |

Shortcut: Say "Catalan number" in the interview. Count of answers: 1, 2, 5, 14, 42 for n = 1 to 5.

## 8. Edge Cases

- `n = 0`: The output is `['']`. The base case occurs at once.
- `n = 1`: The output is `['()']`.

## 9. Common Mistakes

- Do not use `close < n` as the rule for `)`. This makes strings like `")("`. Use `close < open`.
- Do not make all `2^(2n)` strings and filter them. This method is too slow.

## 10. Interview Tips

- Explain the two rules first. Then write the code.
- Say: "I prune invalid branches early, so I never make a bad string."
- Strings in Python are immutable. Thus, `s + '('` makes a new copy. This removes the need to undo.

## 11. Related Problems

- Valid Parentheses (LeetCode 20)
- Remove Invalid Parentheses (LeetCode 301)
- Longest Valid Parentheses (LeetCode 32)
