# 3411. Maximum Subarray With Equal Products

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Array%20%7C%20Math-blue)

## Problem

**LeetCode:** [Maximum Subarray With Equal Products](https://leetcode.com/problems/maximum-subarray-with-equal-products/)

Given an integer array `nums`, find the length of the longest subarray whose product is equal to the product of its greatest common divisor (GCD) and least common multiple (LCM).

For a subarray to be valid:

\[
\text{Product} = \text{GCD} \times \text{LCM}
\]

Return the maximum length of such a subarray.

## Approach: Brute Force with Incremental Updates

Enumerate every possible subarray while maintaining its product, GCD, and LCM incrementally.

Instead of recalculating these values for every subarray, update them whenever a new element is included.

### Algorithm

1. Initialize the maximum valid length to `0`.
2. Iterate through every possible starting index.
3. For each starting index, initialize:
   - `product = 1`
   - `currentGcd = 0`
   - `currentLcm = 1`
4. Extend the subarray by moving the ending index forward.
5. Update the product, GCD, and LCM with the newly included element.
6. If `product === currentGcd * currentLcm`, update the maximum length.
7. Return the maximum length.

## JavaScript Solution

```javascript
/**
 * LeetCode 3411 - Maximum Subarray With Equal Products
 *
 * @param {number[]} nums
 * @return {number}
 */

// Calculate the greatest common divisor.
const gcd = (a, b) => {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }

    return a;
};

// Calculate the least common multiple.
const lcm = (a, b) => {
    return (a / gcd(a, b)) * b;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    const n = nums.length;
    let answer = 0;

    // Establish an upper bound for GCD * LCM.
    let maxLcm = 1;
    let maxValue = 1;

    for (const num of nums) {
        maxLcm = lcm(maxLcm, num);
        maxValue = Math.max(maxValue, num);
    }

    const maxProduct = maxLcm * maxValue;

    // Enumerate every possible starting position.
    for (let left = 0; left < n; left++) {
        let product = 1;
        let currentGcd = 0;
        let currentLcm = 1;

        // Extend the subarray one element at a time.
        for (let right = left; right < n; right++) {
            const num = nums[right];

            product *= num;
            currentGcd = gcd(currentGcd, num);
            currentLcm = lcm(currentLcm, num);

            // Check whether the subarray is product equivalent.
            if (product === currentGcd * currentLcm) {
                answer = Math.max(answer, right - left + 1);
            }

            // The product cannot decrease as the subarray grows.
            if (product > maxProduct) {
                break;
            }
        }
    }

    return answer;
};
```

## Example

**Input:**

```javascript
nums = [2, 3, 4, 5, 6];
```

Consider the subarray `[3, 4, 5]`:

| Property | Calculation | Result |
|---|---|---:|
| Product | 3 × 4 × 5 | 60 |
| GCD | GCD(3, 4, 5) | 1 |
| LCM | LCM(3, 4, 5) | 60 |
| GCD × LCM | 1 × 60 | 60 |

Since the product equals GCD × LCM, this is a valid subarray of length `3`.

**Output:**

```javascript
3
```

## Complexity Analysis

Let `n` represent the length of `nums` and `M` represent its maximum element.

| Complexity | Cost | Explanation |
|---|---|---|
| Time | O(n² log M) | Enumerating subarrays and incrementally calculating GCD and LCM |
| Space | O(1) | Only a fixed number of variables are maintained |

## Key Concepts

- **Subarray Enumeration:** Exploring all contiguous segments of an array.
- **Greatest Common Divisor:** Finding the largest integer that divides all elements.
- **Least Common Multiple:** Finding the smallest positive integer divisible by all elements.
- **Incremental Computation:** Maintaining calculations as a subarray expands.
- **Early Termination:** Avoiding unnecessary work when the running product exceeds the upper bound.

## Important Takeaways

1. Maintain running values when expanding subarrays instead of recalculating them.
2. Euclid's algorithm provides an efficient way to calculate GCD.
3. LCM can be calculated using:

   \[
   LCM(a,b) = \frac{a \times b}{GCD(a,b)}
   \]

4. Understanding mathematical properties can help establish useful bounds for optimization.

## Repository Structure

```text
LeetCode-Solutions/
└── Easy/
    └── JavaScript/
        ├── 3411_Maximum_Subarray_With_Equal_Products.js
        └── README.md
```

## References

- [LeetCode Problem 3411](https://leetcode.com/problems/maximum-subarray-with-equal-products/)
- [Greatest Common Divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor)
- [Least Common Multiple](https://en.wikipedia.org/wiki/Least_common_multiple)

---

**Solution Language:** JavaScript  
**Difficulty:** Easy  
**Topics:** Array, Math, Number Theory

**Author:** [Jeremiah Ogingo](https://github.com/Jeremiahogingo)