# Letter Combinations of a Phone Number

**File:** `letter_combination_of_phone_num.py`
**Topic:** Backtracking — choose, explore, un-choose
**Difficulty:** Medium
**Also known as:** LeetCode 17

---

## 1. Problem

You get a string of digits from `2` to `9`. Each digit maps to letters, as on a phone keypad. Return all letter strings that the digits can make.

| Digit | Letters | Digit | Letters |
|-------|---------|-------|---------|
| 2 | a b c | 6 | m n o |
| 3 | d e f | 7 | p q r s |
| 4 | g h i | 8 | t u v |
| 5 | j k l | 9 | w x y z |

## 2. Examples

| Input | Output |
|-------|--------|
| `"23"` | `['ad','ae','af','bd','be','bf','cd','ce','cf']` |
| `""` | `[]` |
| `"2"` | `['a','b','c']` |

Actual output of the program (`"23"`):

```text
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```

## 3. Key Idea (Shortcut)

> **One digit = one level of the tree.**
> **One letter = one branch.**
> **Pattern: append → recurse → pop.**

The `index` tells you which digit you are on. When `index == len(digits)`, the combination is complete.

## 4. Approach

1. If `digits` is empty, return `[]`.
2. Make a map from each digit to its letters.
3. Call `comboMaker(0, [])`.
4. In `comboMaker`, if `index == len(digits)`, join the list and save it. Then return.
5. Get the letters for `digits[index]`.
6. For each letter, do these three steps:
   1. Append the letter. (Choose)
   2. Call `comboMaker(index + 1, current_ans)`. (Explore)
   3. Pop the letter. (Un-choose)

## 5. Code

```python
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            '2': ['a','b','c'], '3': ['d','e','f'],
            '4': ['g','h','i'], '5': ['j','k','l'],
            '6': ['m','n','o'], '7': ['p','q','r','s'],
            '8': ['t','u','v'], '9': ['w','x','y','z']
        }
        result = []

        def comboMaker(index, current_ans):
            if index == len(digits):
                result.append("".join(current_ans))
                return
            letters = phone_map[digits[index]]
            for letter in letters:
                current_ans.append(letter)     # choose
                comboMaker(index + 1, current_ans)  # explore
                current_ans.pop()              # un-choose

        comboMaker(0, [])
        return result

sol = Solution()
print(sol.letterCombinations('23'))
```

## 6. Recursion Tree ("23")

```text
                   [] (index 0, digit '2')
          /         |          \
        a           b           c        (index 1, digit '3')
      / | \       / | \       / | \
     d  e  f     d  e  f     d  e  f     (index 2 = len -> SAVE)

    ad ae af    bd be bf    cd ce cf
```

## 7. Complexity

| Measure | Value | Reason |
|---------|-------|--------|
| Time | O(4^n · n) | Each digit has at most 4 letters. Joining each answer costs O(n). |
| Space | O(n) | The recursion depth and `current_ans` are both length `n` (not counting the output). |

Here, `n` is the number of digits.

## 8. Edge Cases

- Empty input `""`: Return `[]`, not `['']`. The early `if not digits` check does this.
- Input with `7` or `9`: These digits have 4 letters. Do not assume 3 letters for each digit.
- Input with `0` or `1`: These digits are not in the map. The code gets `KeyError`. Ask the interviewer if these digits can occur.

## 9. Common Mistakes

- Do not forget `pop()`. Without it, old letters stay in the list.
- Do not append `current_ans` directly. Use `"".join(current_ans)` to make a new string.

## 10. Interview Tips

- Say the template aloud: "choose, explore, un-choose."
- Short Python alternative: `["".join(p) for p in itertools.product(*(phone_map[d] for d in digits))]`. Mention it, but write the backtracking version first.
- An iterative (BFS) version is also possible. Start with `['']`. For each digit, extend each string with each letter.

## 11. Related Problems

- Generate Parentheses (LeetCode 22)
- Combinations (LeetCode 77)
- Permutations (LeetCode 46)
