# 60. Permutation Sequence

![LeetCode](https://img.shields.io/badge/LeetCode-60-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-Java-blue?logo=openjdk)
![Algorithm](https://img.shields.io/badge/Algorithm-Combinatorics-success)

## Problem Overview

Given two integers, `n` and `k`, find the `k`-th permutation of the numbers from `1` to `n`, considering all permutations in lexicographical order.

There are \(n!\) possible permutations. Instead of generating and sorting every permutation, we can determine each digit directly using factorials.

**LeetCode:** [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

## Approach: Factorial Number System

The key observation is that fixing the first digit divides the permutations into blocks of \((n-1)!\) permutations. Fixing the next digit divides the remaining possibilities into blocks of \((n-2)!\), and so on.

We use these block sizes to select the correct digit at every position.

### Algorithm

1. Precompute factorials from `0!` through `n!`.
2. Store the available numbers in a list: `[1, 2, ..., n]`.
3. Convert `k` to zero-based indexing by subtracting `1`.
4. For each remaining position:
   - Calculate the block size using the factorial of the remaining positions.
   - Divide `k` by the block size to find the index of the next number.
   - Append that number to the result and remove it from the available numbers.
   - Update `k` using the remainder.
5. Return the completed permutation as a string.

## Java Implementation

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String getPermutation(int n, int k) {
        int[] factorial = new int[n + 1];
        factorial[0] = 1;

        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        List<Integer> numbers = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        // Convert from 1-based to 0-based indexing.
        k--;

        StringBuilder result = new StringBuilder();

        for (int remaining = n; remaining > 0; remaining--) {
            int blockSize = factorial[remaining - 1];
            int index = k / blockSize;

            result.append(numbers.remove(index));

            k %= blockSize;
        }

        return result.toString();
    }
}
```

## Example Walkthrough

**Input:**

```text
n = 4, k = 9
```

The available numbers initially are `[1, 2, 3, 4]`. Convert `k = 9` to the zero-based index `8`.

| Position | Block size | Index selected | Chosen digit | Remaining numbers | New `k` |
|---|---:|---:|---:|---|---:|
| 1 | `3! = 6` | `8 / 6 = 1` | `2` | `[1, 3, 4]` | `2` |
| 2 | `2! = 2` | `2 / 2 = 1` | `3` | `[1, 4]` | `0` |
| 3 | `1! = 1` | `0 / 1 = 0` | `1` | `[4]` | `0` |
| 4 | `0! = 1` | `0 / 1 = 0` | `4` | `[]` | `0` |

**Output:**

```text
"2314"
```

The algorithm selects the correct permutation directly without generating the other 23 permutations.

## Edge Cases

| Input `(n, k)` | Expected Output | Explanation |
|---|---|---|
| `(1, 1)` | `"1"` | Only one number and one permutation |
| `(3, 1)` | `"123"` | First permutation in lexicographical order |
| `(3, 6)` | `"321"` | Last permutation for `n = 3` |
| `(3, 3)` | `"213"` | Middle permutation selected by its rank |
| `(4, 9)` | `"2314"` | Selects the ninth permutation |
| `(4, 24)` | `"4321"` | Last permutation for `n = 4` |

The solution relies on the problem constraints: `1 <= n <= 9` and `1 <= k <= n!`. Inputs outside these constraints are not validated by this implementation.

## Complexity Analysis

- **Time Complexity:** \(O(n^2)\) — factorial computation takes \(O(n)\), while removing an element from an `ArrayList` can take \(O(n)\). Repeating this for `n` positions gives \(O(n^2)\).
- **Auxiliary Space Complexity:** \(O(n)\) — the factorial array, available-number list, and result string require linear space.

## Zero Based Indexing explained — Permutation Sequence:
 The zero-based indexing conversion is this line:

```
k--;
```

It converts `k` from a 1-based position (counting starts at 1) into a 0-based index (counting starts at 0).

## 1. Why is the conversion necessary?

Suppose `n = 3`. The permutations in lexicographical order are:

| `k` (problem position) | Permutation | Zero-based index |
| ---------------------- | ----------- | ---------------- |
| 1                      | `123`       | 0                |
| 2                      | `132`       | 1                |
| 3                      | `213`       | 2                |
| 4                      | `231`       | 3                |
| 5                      | `312`       | 4                |
| 6                      | `321`       | 5                |

The problem asks for the 1st, 2nd, 3rd, ... permutation, so `k` starts at 1. However, Java lists use indices starting at 0.

Therefore:

\\[ \text{zero-based index}=k-1 \\]

For example, if `k = 4`, the requested permutation is `231`. Its zero-based index is `3`.

## 2. How does this affect the factorial calculation?

Consider `n = 4`, `k = 9`.

There are \\(3! = 6\\) permutations for each possible first digit. After converting `k`:

```
k--;  // 9 becomes 8
```

We calculate:

```
int blockSize = factorial[3];  // 6
int index = k / blockSize;     // 8 / 6 = 1
```

The available numbers are `[1, 2, 3, 4]`.

- Index `0` selects `1`.
- Index `1` selects `2`.
- Index `2` selects `3`.
- Index `3` selects `4`.

Since `index = 1`, we select `2` as the first digit.

Next, we calculate the position within that block:

```
k %= blockSize;  // 8 % 6 = 2
```

The remaining zero-based position is now `2`, and we continue selecting the remaining digits.

The final result is `"2314"`.

## 3. What if we forget `k--`?

With `k = 9`, the first index would be:

\\[ 9 / 6 = 1 \\]

Java's integer division still gives `1` here, so the first digit happens to be correct. But the remainder would be:

\\[ 9 \bmod 6 = 3 \\]

Instead of `2`, which is the correct zero-based remainder. This can cause later digits to be selected incorrectly or lead to an invalid list index in other cases.

Remember: `k--` is necessary because the problem numbers permutations starting at `1`, while the algorithm uses zero-based list indices and arithmetic.

## Key Takeaways

- Factorials help count permutations without enumerating them.
- The `k--` conversion is essential because Java list indices are zero-based.
- Integer division identifies the correct permutation block.
- Modulo tracks the position within the selected block.
- Removing each chosen number ensures that every digit appears exactly once.
- This technique is an example of **factorial-number-system unranking**: constructing a permutation from its lexicographical rank.

## Related Problems

- [Permutations](https://leetcode.com/problems/permutations/)
- [Next Permutation](https://leetcode.com/problems/next-permutation/)
- [Permutations II](https://leetcode.com/problems/permutations-ii/)

---
