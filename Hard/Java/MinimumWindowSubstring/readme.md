# 🔍 Minimum Window Substring

![LeetCode](https://img.shields.io/badge/LeetCode-76-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)
![Language](https://img.shields.io/badge/Language-Java-orange?style=flat-square\&logo=openjdk)
![Time](https://img.shields.io/badge/Time-O\(m%2Bn\)-blue?style=flat-square)
![Space](https://img.shields.io/badge/Space-O\(1\)-blue?style=flat-square)

## Overview

Given strings `s` and `t`, find the minimum-length substring of `s` containing every character in `t`, including duplicate occurrences.

Return an empty string if no valid window exists.

### Example

```text
Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"
```

## Approach

Use a **sliding window** and a character-frequency array.

1. **Count required characters:** Record the frequency of each character in `t`.
2. **Expand the window:** Move the right pointer through `s`, tracking how many required character occurrences remain.
3. **Shrink the window:** Once all requirements are satisfied, move the left pointer forward while updating the shortest valid window.
4. **Return the result:** Extract the shortest valid substring, or return `""` if none exists.

The `missing` variable tracks the number of character occurrences still required. This correctly handles duplicate characters.

## Implementation

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        int[] count = new int[128];

        for (char c : t.toCharArray()) {
            count[c]++;
        }

        int left = 0;
        int start = 0;
        int minLength = Integer.MAX_VALUE;
        int missing = t.length();

        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);

            if (count[current] > 0) {
                missing--;
            }
            count[current]--;

            while (missing == 0) {
                int windowLength = right - left + 1;

                if (windowLength < minLength) {
                    minLength = windowLength;
                    start = left;
                }

                char leftChar = s.charAt(left);
                count[leftChar]++;

                if (count[leftChar] > 0) {
                    missing++;
                }

                left++;
            }
        }

        return minLength == Integer.MAX_VALUE
                ? ""
                : s.substring(start, start + minLength);
    }
}
```

## Example Walkthrough

For `s = "ADOBECODEBANC"` and `t = "ABC"`:

| Window   | Length | Result                 |
| -------- | -----: | ---------------------- |
| `ADOBEC` |      6 | First valid window     |
| `EBANC`  |      5 | A shorter valid window |
| `BANC`   |      4 | Minimum window         |

Final output: `"BANC"`

## Edge Cases

| Case                   | Input                      | Output  | Behavior                             |
| ---------------------- | -------------------------- | ------- | ------------------------------------ |
| Exact match            | `s = "a", t = "a"`         | `"a"`   | Entire string is the answer          |
| No valid window        | `s = "a", t = "aa"`        | `""`    | Required occurrences are unavailable |
| Duplicate characters   | `s = "aa", t = "aa"`       | `"aa"`  | Both occurrences are required        |
| Case sensitivity       | `s = "aA", t = "A"`        | `"A"`   | Uppercase and lowercase differ       |
| `t` longer than `s`    | `s = "ab", t = "abc"`      | `""`    | Returns immediately                  |
| Multiple valid windows | `s = "abdabca", t = "abc"` | `"abc"` | Returns the shortest valid window    |

## Complexity

Let `m` be the length of `s` and `n` the length of `t`.

| Metric          | Complexity   |
| --------------- | ------------ |
| Time            | **O(m + n)** |
| Auxiliary space | **O(1)**     |

Each pointer advances at most `m` times, and the frequency array has a fixed size of 128 entries.

## Key Takeaways

* Sliding windows efficiently solve substring problems.
* Character frequencies handle duplicates correctly.
* Shrinking a valid window helps find the minimum length.
* Each character is processed a constant number of times.

## Related Problems

* [#3 — Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* [#209 — Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
* [#438 — Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
* [#567 — Permutation in String](https://leetcode.com/problems/permutation-in-string/)

## Reference

[LeetCode — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

<div align="center">

**Expand → Validate → Shrink → Optimize**

</div>
