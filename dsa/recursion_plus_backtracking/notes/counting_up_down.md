# Counting Up and Down (Bounce)

**File:** `counting_up_down.py`
**Topic:** Recursion basics — work before and after the recursive call
**Difficulty:** Easy

---

## 1. Problem

Print the numbers from `n` down to `1`. Then print the numbers from `1` up to `n`.
Use one recursive function. Do not use a loop.

## 2. Example

| Input | Output |
|-------|--------|
| `bounce(3)` | `3 2 1 1 2 3` (one number on each line) |

Actual output of the program:

```text
3
2
1
1
2
3
```

## 3. Key Idea (Shortcut)

> **Code before the call runs on the way DOWN.**
> **Code after the call runs on the way BACK UP.**

Each function call waits on the call stack. When the base case returns, each waiting call continues. This return phase is the base of all backtracking.

## 4. Approach

1. Stop when `n` is `0`. This is the base case.
2. Print `n`. This step runs on the way down.
3. Call `bounce(n - 1)`.
4. Print `n` again. This step runs on the way back up.

## 5. Code

```python
def bounce(n):
    if n == 0:
        return
    print(n)      # Task A: on the way DOWN
    bounce(n - 1) # Recurse
    print(n)      # Task B: on the way BACK UP (backtrack phase)

bounce(3)
```

## 6. Dry Run (n = 3)

```text
bounce(3) -> print 3
  bounce(2) -> print 2
    bounce(1) -> print 1
      bounce(0) -> return        (base case)
    bounce(1) -> print 1         (back up)
  bounce(2) -> print 2           (back up)
bounce(3) -> print 3             (back up)
```

## 7. Complexity

| Measure | Value | Reason |
|---------|-------|--------|
| Time | O(n) | The function makes one call for each value from `n` to `0`. |
| Space | O(n) | The call stack holds `n` frames at the deepest point. |

## 8. Edge Cases

- `n = 0`: The function prints nothing.
- Negative `n`: The base case never occurs. The program gets `RecursionError`. Use `if n <= 0` to prevent this.
- Large `n` (more than about 1000): Python gets `RecursionError`. The default recursion limit is 1000.

## 9. Interview Tips

- Use this example to explain the call stack. Interviewers like a clear stack drawing.
- To print only `1` to `n`, remove the first `print`.
- To print only `n` to `1`, remove the second `print`.
- Remember the rule: "Before the call = going down. After the call = coming back."

## 10. Related Problems

- Print 1 to N without a loop
- Reverse a string with recursion
- Factorial and sum of first N numbers
