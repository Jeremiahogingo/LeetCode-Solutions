# 3789. Minimum Cost to Acquire Required Items

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Greedy%20%7C%20Math-purple)
![LeetCode](https://img.shields.io/badge/LeetCode-3789-blue)

## Problem

**[Minimum Cost to Acquire Required Items](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/)**

You are given five integers:

- `cost1`: Cost of an item that contributes one unit toward requirement 1.
- `cost2`: Cost of an item that contributes one unit toward requirement 2.
- `costBoth`: Cost of an item that contributes one unit toward both requirements.
- `need1`: Minimum units required for requirement 1.
- `need2`: Minimum units required for requirement 2.

There are three types of items:

| Item Type | Cost | Contribution |
|---|---:|---|
| Type 1 | `cost1` | Requirement 1 only |
| Type 2 | `cost2` | Requirement 2 only |
| Type 3 | `costBoth` | Requirements 1 and 2 |

Return the minimum total cost needed to satisfy both requirements.

Buying extra units is allowed.

## Approach: Greedy Cost Optimization

The key observation is that a type 3 item contributes toward both requirements simultaneously.

Instead of checking every possible purchasing combination, we can divide the requirements into two parts:

1. The common requirement shared by both types.
2. Any remaining units needed by either individual requirement.

### 1. Calculate the Common Requirement

The number of units shared by both requirements is:

```javascript
const common = Math.min(need1, need2);
```

For each common unit, we have two choices:

- Buy one type 3 item for `costBoth`.
- Buy one type 1 item and one type 2 item for `cost1 + cost2`.

Therefore, the cheapest cost per common unit is:

```javascript
const sharedCost = Math.min(costBoth, cost1 + cost2);
```

### 2. Calculate the Remaining Requirements

After satisfying the common requirement, only one requirement can have remaining units.

For the remaining type 1 units, choose between:

- A type 1 item costing `cost1`.
- A type 3 item costing `costBoth`.

The cheapest option is:

```javascript
Math.min(cost1, costBoth)
```

Similarly, for the remaining type 2 units:

```javascript
Math.min(cost2, costBoth)
```

Buying a type 3 item for an extra unit is valid because exceeding an already-satisfied requirement is allowed.

### 3. Calculate the Minimum Total Cost

The final formula is:

\[
\begin{aligned}
\text{Total Cost} ={}&
\text{common}\times\text{sharedCost}\\
&+(\text{need1}-\text{common})\times\min(\text{cost1},\text{costBoth})\\
&+(\text{need2}-\text{common})\times\min(\text{cost2},\text{costBoth})
\end{aligned}
\]

This considers the cheapest purchase option for every part of the requirements without enumerating combinations.

## JavaScript Solution

```javascript
/**
 * LeetCode 3789 - Minimum Cost to Acquire Required Items
 *
 * @param {number} cost1
 * @param {number} cost2
 * @param {number} costBoth
 * @param {number} need1
 * @param {number} need2
 * @return {number}
 */
var minimumCost = function(cost1, cost2, costBoth, need1, need2) {
    // Find the number of units shared by both requirements.
    const common = Math.min(need1, need2);

    // Choose between a shared item and two individual items.
    const sharedCost = Math.min(costBoth, cost1 + cost2);

    let totalCost = common * sharedCost;

    // Handle remaining type 1 requirements.
    totalCost += (need1 - common) * Math.min(cost1, costBoth);

    // Handle remaining type 2 requirements.
    totalCost += (need2 - common) * Math.min(cost2, costBoth);

    return totalCost;
};
```

## Examples and Dry Runs

### Example 1: Shared Items Are Cheaper

**Input:**

```javascript
cost1 = 3;
cost2 = 2;
costBoth = 1;
need1 = 3;
need2 = 2;
```

**Step 1: Calculate the common requirement.**

\[
common=\min(3,2)=2
\]

**Step 2: Find the cheapest common-unit cost.**

\[
sharedCost=\min(1,3+2)=1
\]

**Step 3: Calculate the total cost.**

Common requirement:

\[
2\times1=2
\]

Remaining type 1 requirement:

\[
(3-2)\times\min(3,1)=1
\]

Remaining type 2 requirement:

\[
(2-2)\times\min(2,1)=0
\]

Final cost:

\[
2+1+0=\boxed{3}
\]

**Output:**

```javascript
3
```

**Explanation:** Buying three type 3 items costs 3 and satisfies both requirements.

### Example 2: Individual Items Are Cheaper

**Input:**

```javascript
cost1 = 5;
cost2 = 4;
costBoth = 15;
need1 = 2;
need2 = 3;
```

**Step 1: Calculate the common requirement.**

\[
common=\min(2,3)=2
\]

**Step 2: Find the cheapest common-unit cost.**

\[
sharedCost=\min(15,5+4)=9
\]

**Step 3: Calculate the total cost.**

Common requirement:

\[
2\times9=18
\]

Remaining type 1 requirement:

\[
(2-2)\times5=0
\]

Remaining type 2 requirement:

\[
(3-2)\times\min(4,15)=4
\]

Final cost:

\[
18+4=\boxed{22}
\]

**Output:**

```javascript
22
```

**Explanation:** Buying two type 1 items and three type 2 items costs 22, which is cheaper than purchasing type 3 items.

### Example 3: No Items Required

**Input:**

```javascript
cost1 = 5;
cost2 = 4;
costBoth = 15;
need1 = 0;
need2 = 0;
```

Both requirements are already satisfied.

**Output:**

```javascript
0
```

## Complexity Analysis

The solution uses a fixed number of arithmetic operations and comparisons.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(1)` | No loops or iterations over the required quantities |
| Auxiliary Space | `O(1)` | Only a constant number of variables |

**Time Complexity: `O(1)`**

The minimum cost is calculated directly using arithmetic operations and `Math.min()`.

**Space Complexity: `O(1)`**

The algorithm uses constant additional memory regardless of the input values.

### Integer Precision

The constraints allow `need1` and `need2` to reach \(10^9\), while item costs can reach \(10^6\).

The maximum individual-purchase total is:

\[
10^9\times10^6+10^9\times10^6=2\times10^{15}
\]

This is below JavaScript's maximum safe integer of \(2^{53}-1\), so the standard JavaScript `Number` type safely represents the result under the given constraints.

## Important Edge Cases

| Scenario | Expected Behavior |
|---|---|
| Both requirements are zero | Return `0` |
| Type 3 is cheaper than both individual items combined | Prefer type 3 for common units |
| Type 3 is more expensive than individual items combined | Prefer individual items for common units |
| Only requirement 1 is positive | Choose the cheaper of type 1 and type 3 |
| Only requirement 2 is positive | Choose the cheaper of type 2 and type 3 |
| One requirement is larger than the other | Satisfy the common portion, then optimize the remaining units |
| Type 3 is cheaper than an individual item | It may be optimal to purchase extra type 3 items |

## Key Takeaways

- Greedy optimization can eliminate unnecessary enumeration in cost-minimization problems.
- Shared resources should be compared against the combined cost of individual resources.
- Buying extra units can be optimal when the shared option is cheaper.
- Splitting an optimization problem into common and remaining requirements simplifies the calculation.
- Always consider whether a combined purchase is cheaper for both shared and excess requirements.
- Mathematical optimization can produce constant-time solutions even when input quantities are very large.

## Related Problems

- [LeetCode 322 – Coin Change](https://leetcode.com/problems/coin-change/)
- [LeetCode 860 – Lemonade Change](https://leetcode.com/problems/lemonade-change/)
- [LeetCode 1217 – Minimum Cost to Move Chips to The Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)
- [LeetCode 1266 – Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── JavaScript/
        ├── 3789_Minimum_Cost_to_Acquire_Required_Items.js
        └── README.md
```

## References

- [LeetCode – Minimum Cost to Acquire Required Items](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/)
- [LeetCode Constraints and Hints](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/)

---

**Problem:** 3789  
**Difficulty:** Medium  
**Language:** JavaScript  
**Topics:** Greedy, Mathematics, Cost Optimization  
**Time Complexity:** `O(1)`  
**Auxiliary Space:** `O(1)`