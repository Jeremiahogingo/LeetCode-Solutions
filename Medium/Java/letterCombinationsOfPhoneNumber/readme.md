# LeetCode 17: Letter Combinations of a Phone Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Java-orange)
![Topic](https://img.shields.io/badge/Topic-Backtracking-blue)

## Problem Description

Given a string containing digits from `2` to `9`, return all possible letter combinations that the number could represent using the letters mapped to each digit on a telephone keypad.

Return the combinations in any order. If the input string is empty, return an empty list.

**Problem link:** [LeetCode 17 — Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

## Approach: Backtracking

Backtracking explores every possible combination by choosing one letter for each digit.

1. Map each digit to its corresponding letters on a telephone keypad.
2. Start with an empty combination and process the digits from left to right.
3. Append each possible letter for the current digit.
4. Recursively process the next digit.
5. Once all digits have been processed, add the completed combination to the result.
6. Remove the last letter and explore the next possibility.

A `StringBuilder` efficiently constructs combinations without repeatedly creating intermediate strings.

## Java Solution

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[] KEYPAD = {
        "", "", "abc", "def", "ghi",
        "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();

        if (digits == null || digits.isEmpty()) {
            return result;
        }

        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(
        String digits,
        int index,
        StringBuilder current,
        List<String> result
    ) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        String letters = KEYPAD[digits.charAt(index) - '0'];

        for (int i = 0; i < letters.length(); i++) {
            current.append(letters.charAt(i));

            backtrack(digits, index + 1, current, result);

            current.deleteCharAt(current.length() - 1);
        }
    }
}
```

## Examples

**Example 1**

- Input: `digits = "23"`
- Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
- Explanation: Digit `2` maps to `abc`, while digit `3` maps to `def`. Combining each letter from the first group with each letter from the second produces nine combinations.

**Example 2**

- Input: `digits = ""`
- Output: `[]`
- Explanation: An empty input produces no combinations.

**Example 3**

- Input: `digits = "2"`
- Output: `["a","b","c"]`
- Explanation: Each letter mapped to digit `2` forms a separate combination.

## Complexity Analysis

Let \(n\) be the number of digits, and let \(k\) be the maximum number of letters mapped to a digit, where \(k = 4\).

- **Time Complexity:** \(O(n \cdot 4^n)\) — up to \(4^n\) combinations may be generated, each requiring \(O(n)\) time to materialize.
- **Auxiliary Space Complexity:** \(O(n)\) — the recursion stack and current combination require linear space, excluding the output.
- **Output Space Complexity:** \(O(n \cdot 4^n)\) in the worst case.

## Key Takeaways

- Backtracking systematically explores all possible choices.
- Each recursive call processes one digit.
- Undoing a choice allows the algorithm to explore alternative combinations.
- `StringBuilder` reduces the overhead of constructing strings during recursion.
- The number of combinations grows exponentially with the number of digits.

## References

- [LeetCode Problem 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
- [Java StringBuilder Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)
