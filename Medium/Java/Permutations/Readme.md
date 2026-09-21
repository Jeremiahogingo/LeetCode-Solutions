# 🔄 Permutations

![LeetCode](https://img.shields.io/badge/LeetCode-46-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Java-17%2B-red?style=flat-square\&logo=openjdk)
![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-blue?style=flat-square)

## 📌 Overview

Given an array of **distinct integers**, return all possible permutations.

### Example

```text
Input:  [1,2,3]

Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

The number of permutations is:

```text
n!
```

---

## 🧠 Approach

Use **backtracking** to construct each permutation:

1. Start with an empty permutation.
2. Try every unused number.
3. Mark the number as used and add it to the current permutation.
4. Recursively continue until the permutation is complete.
5. Remove the last number and mark it unused.
6. Try the next possibility.

The process follows:

```text
Choose → Explore → Undo
```

---

## 💻 Implementation

```java
import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];

        backtrack(nums, used, new ArrayList<>(), result);

        return result;
    }

    private void backtrack(
            int[] nums,
            boolean[] used,
            List<Integer> current,
            List<List<Integer>> result
    ) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }

            used[i] = true;
            current.add(nums[i]);

            backtrack(nums, used, current, result);

            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}
```

---

## 🔍 Example Walkthrough

For:

```text
nums = [1,2,3]
```

The recursion explores:

```text
                []
          /      |      \
        [1]     [2]     [3]
       /  \     /  \     /  \
    [1,2] [1,3] ...
```

Starting with `1`:

```text
[1]
 ├── [1,2]
 │    └── [1,2,3]
 └── [1,3]
      └── [1,3,2]
```

After finishing a branch, backtracking removes the last element and tries another unused number.

---

## ⚠️ Edge Cases

| Case             | Input    | Output                 | Behavior                                |
| ---------------- | -------- | ---------------------- | --------------------------------------- |
| Empty array      | `[]`     | `[[]]`                 | The empty permutation is generated      |
| One element      | `[1]`    | `[[1]]`                | Only one permutation exists             |
| Two elements     | `[1,2]`  | `[[1,2],[2,1]]`        | Both orderings are generated            |
| Negative values  | `[-1,2]` | `[[-1,2],[2,-1]]`      | Values are handled normally             |
| Duplicate values | `[1,1]`  | Duplicate permutations | Problem assumes all values are distinct |

---

## ⏱️ Complexity

For `n` elements:

* **Time:** `O(n × n!)`
* **Auxiliary Space:** `O(n)`
* **Output Space:** `O(n × n!)`

There are `n!` possible permutations, and copying each completed permutation takes `O(n)`.

---

## 💡 Key Takeaways

* Backtracking is ideal for generating permutations.
* A `boolean[]` efficiently tracks used elements.
* Every recursive call represents one position in the permutation.
* Always **undo the choice** before exploring the next option.
* With distinct elements, the total number of permutations is `n!`.

---

## 🔗 Related Problems

* **#47 — Permutations II** → Backtracking with duplicate handling
* **#77 — Combinations** → Backtracking without considering order
* **#78 — Subsets** → Generate all subsets
* **#39 — Combination Sum** → Backtracking with reusable choices
* **#51 — N-Queens** → Constraint-based backtracking

---

## 📁 Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Java/
        └── Permutations/
            ├── Solution.java
            └── README.md
```

---

## 📖 Reference

[LeetCode — Permutations](https://leetcode.com/problems/permutations/)

---

<div align="center">

⭐ **Backtracking — Choose → Explore → Undo**

</div>
