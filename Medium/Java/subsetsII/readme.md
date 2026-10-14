# 🔢 Subsets II

![LeetCode](https://img.shields.io/badge/LeetCode-90-orange?style=flat-square&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Language-Java-orange?style=flat-square&logo=openjdk)
![Time](https://img.shields.io/badge/Time-O(n·2ⁿ)-blue?style=flat-square)
![Space](https://img.shields.io/badge/Space-O(n)-blue?style=flat-square)

## Overview

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set) without including duplicate subsets.

The solution must preserve valid subsets containing repeated values.

### Example

```text
Input:
nums = [1, 2, 2]

Output:
[[], [1], [1,2], [1,2,2], [2], [2,2]]
```

## Approach

Use **backtracking with sorting and duplicate skipping**.

1. **Sort the array:** Place equal values next to each other.
2. **Record each subset:** Add a copy of the current subset to the result at every recursive call.
3. **Skip duplicates:** Ignore a repeated value when it appears at the same recursion level.
4. **Backtrack:** Remove the last selected value and explore the next possibility.

The condition `i > start && nums[i] == nums[i - 1]` prevents duplicate subsets without removing valid combinations such as `[2, 2]`.

## Implementation

```java
import java.util.*;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);

        return result;
    }

    private void backtrack(
            int[] nums,
            int start,
            List<Integer> current,
            List<List<Integer>> result
    ) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }

            current.add(nums[i]);

            backtrack(nums, i + 1, current, result);

            current.remove(current.size() - 1);
        }
    }
}
```

## Example Walkthrough

For `nums = [1, 2, 2]`:

```text
[]
├── [1]
│   └── [1, 2]
│       └── [1, 2, 2]
└── [2]
    └── [2, 2]
```

The algorithm skips the second `2` when it would create a duplicate choice at the same recursion level. It can still select both occurrences along the same path.

## Edge Cases

| Case | Input | Behavior |
|---|---|---|
| Single element | `[0]` | Returns `[]` and `[0]` |
| All elements equal | `[2, 2]` | Returns `[]`, `[2]`, `[2, 2]` |
| All elements distinct | `[1, 2, 3]` | Returns all 8 subsets |
| Negative values | `[-1, 0, 0]` | Produces unique subsets with negative and repeated values |
| Empty array | `[]` | Returns `[[]]` |

## Complexity

Let \(n\) be the number of elements.

| Metric | Complexity |
|---|---|
| Time | **O(n × 2ⁿ)** |
| Auxiliary space | **O(n)** |
| Output space | **O(n × 2ⁿ)** in the worst case |

Sorting takes \(O(n \log n)\), while generating and copying subsets dominates the overall time complexity.

## Key Takeaways

- Backtracking explores all valid combinations.
- Sorting makes duplicate detection straightforward.
- Skip duplicates only at the same recursion level.
- Copy the current subset before adding it to the result.

## Related Problems

- [#78 — Subsets](https://leetcode.com/problems/subsets/)
- [#46 — Permutations](https://leetcode.com/problems/permutations/)
- [#47 — Permutations II](https://leetcode.com/problems/permutations-ii/)
- [#39 — Combination Sum](https://leetcode.com/problems/combination-sum/)

## Reference

[LeetCode — Subsets II](https://leetcode.com/problems/subsets-ii/)

---

<div align="center">

**Sort → Backtrack → Skip Duplicates**

</div>