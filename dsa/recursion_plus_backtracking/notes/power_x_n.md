# Pow(x, n) — Fast Power

**File:** `power_x_n.py`
**Topic:** Recursion — divide and conquer (binary exponentiation)
**Difficulty:** Medium
**Also known as:** LeetCode 50

---

## 1. Problem

Calculate `x` raised to the power `n` (`x^n`). The value `n` can be negative. Do not use `**` or `pow()`.

## 2. Examples

| Input | Output |
|-------|--------|
| `x = 2, n = 10` | `1024` |
| `x = 2, n = -2` | `0.25` |
| `x = 2.1, n = 3` | `9.261` (approximately) |
| `x = 5, n = 0` | `1` |

Actual output of the program (`myPow(2, 10)`):

```text
1024
```

## 3. Key Idea (Shortcut)

> **If `n` is even: `x^n = (x*x)^(n/2)`.**
> **If `n` is odd: `x^n = x * x^(n-1)`.**
> **If `n` is negative: `x^n = 1 / x^(-n)`.**

Each even step cuts `n` in half. Thus, the method needs about `log n` steps, not `n` steps.

## 4. Approach

1. If `n` is negative, calculate `power(x, -n)`. Then return `1 / result`.
2. In `power(x, n)`:
   1. If `n == 0`, return `1`.
   2. If `n == 1`, return `x`.
   3. If `n` is odd, return `x * power(x, n - 1)`.
   4. If `n` is even, return `power(x * x, n // 2)`.

## 5. Code

```python
class Solution:
    def power(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2:
            return x * self.power(x, n - 1)
        else:
            return self.power(x * x, n // 2)

    def myPow(self, x, n):
        num = n
        if num < 0:
            return 1.0 / self.power(x, -num)
        return self.power(x, num)

sol = Solution()
print(sol.myPow(2, 10))
```

## 6. Dry Run (x = 2, n = 10)

```text
power(2, 10)   even -> power(4, 5)
power(4, 5)    odd  -> 4 * power(4, 4)
power(4, 4)    even -> power(16, 2)
power(16, 2)   even -> power(256, 1)
power(256, 1)  base -> 256

Back up: 4 * 256 = 1024
```

The method uses 5 calls. A simple loop uses 10 multiplications.

## 7. Complexity

| Approach | Time | Space |
|----------|------|-------|
| Simple loop (`x * x * ...`) | O(n) | O(1) |
| This method (fast power) | O(log n) | O(log n) for the call stack |
| Iterative fast power | O(log n) | O(1) |

## 8. Edge Cases

- `n = 0`: Return `1`, also for `x = 0` (by convention).
- Negative `n`: Return `1 / x^(-n)`. The code does this in `myPow`.
- `x = 0` and negative `n`: The code gets `ZeroDivisionError`. Ask the interviewer how to handle this.
- `n = -2^31`: In Java or C++, `-n` overflows an `int`. Use a `long`. In Python, this problem does not occur.

## 9. Common Mistakes

- Do not calculate `power(x, n // 2)` two times. This makes the time O(n) again. Calculate it one time and save it.
- Do not forget the negative `n` case.

## 10. Interview Tips

- Say "binary exponentiation" or "exponentiation by squaring."
- Show the other common form:

  ```python
  def power(x, n):
      if n == 0:
          return 1
      half = power(x, n // 2)
      return half * half if n % 2 == 0 else half * half * x
  ```

- If the interviewer asks for O(1) space, use the iterative version:

  ```python
  def my_pow(x, n):
      if n < 0:
          x, n = 1 / x, -n
      result = 1
      while n:
          if n & 1:
              result *= x
          x *= x
          n >>= 1
      return result
  ```

## 11. Related Problems

- Super Pow (LeetCode 372)
- Modular exponentiation (`(x^n) % m`)
- Count Good Numbers (LeetCode 1922)
