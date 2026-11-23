# 1352. Product of the Last K Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Approach](https://img.shields.io/badge/Approach-Prefix_Products-blue)
![Time Complexity](https://img.shields.io/badge/Add%2FGetProduct-O(1)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space-O(n)-brightgreen)

## Problem

**LeetCode:** [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/)

**Difficulty:** Medium

**Language:** JavaScript

Design a data structure that supports two operations on a stream of integers:

- `add(num)`: Appends an integer to the stream.
- `getProduct(k)`: Returns the product of the last `k` integers in the stream.

The goal is to implement both operations efficiently.

## Approach: Prefix Products with Zero Reset

Instead of multiplying the last `k` numbers every time `getProduct(k)` is called, we maintain an array of cumulative products.

This allows us to calculate range products using division.

### 1. Prefix Product Concept

Consider the following stream:

```text
Numbers:         [3, 2, 5, 4]
Prefix products: [1, 3, 6, 30, 120]
```

Each prefix product represents the cumulative product of all preceding numbers.

To obtain the product of the last two numbers:

\[
\frac{120}{6}=20
\]

In general:

\[
\text{Product}(k)=
\frac{prefix[n]}{prefix[n-k]}
\]

Where:
- `n` is the number of values stored since the most recent zero.
- `prefix[n]` is the latest cumulative product.
- `prefix[n-k]` is the cumulative product immediately before the requested range.

### 2. Handling Zero

Zero requires special handling because division by a prefix product containing zero is invalid.

Whenever `add(0)` is called, reset the prefix array to:

```javascript
[1]
```

This effectively starts a new prefix-product sequence.

If `getProduct(k)` requests more numbers than are available since the latest zero, the requested range must contain zero. Therefore, return `0`.

## JavaScript Solution

**File:** `1352_Product_of_the_Last_K_Numbers.js`

```javascript
/**
 * LeetCode 1352 - Product of the Last K Numbers
 *
 * @constructor
 */
var ProductOfNumbers = function() {
    // Sentinel value simplifies prefix product calculations.
    this.prefixProducts = [1];
};

/**
 * Appends a number to the stream.
 *
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    // Zero invalidates every prefix product that spans it.
    if (num === 0) {
        this.prefixProducts = [1];
        return;
    }

    const lastProduct =
        this.prefixProducts[this.prefixProducts.length - 1];

    // Store the cumulative product.
    this.prefixProducts.push(lastProduct * num);
};

/**
 * Returns the product of the last k numbers.
 *
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    const n = this.prefixProducts.length;

    // The requested range includes a zero.
    if (k >= n) {
        return 0;
    }

    // Divide the latest prefix product by the
    // prefix product immediately before the range.
    return (
        this.prefixProducts[n - 1] /
        this.prefixProducts[n - 1 - k]
    );
};
```

## Example Walkthrough

### Example 1

**Input:**

```text
["ProductOfNumbers", "add", "add", "add", "add", "add",
 "getProduct", "getProduct", "getProduct", "add", "getProduct"]

[[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
```

**Output:**

```text
[null, null, null, null, null, null, 20, 40, 0, null, 32]
```

### Step-by-step execution

**Step 1: Initialize**

```text
prefixProducts = [1]
```

**Step 2: Add 3**

```text
Stream:          [3]
Prefix products: [1, 3]
```

**Step 3: Add 0**

The zero resets the prefix-product history.

```text
Stream:          [3, 0]
Prefix products: [1]
```

**Step 4: Add 2, 5 and 4**

```text
Stream:          [3, 0, 2, 5, 4]
Prefix products: [1, 2, 10, 40]
```

**Step 5: getProduct(2)**

\[
\frac{40}{2}=20
\]

Result: `20`

**Step 6: getProduct(3)**

\[
\frac{40}{1}=40
\]

Result: `40`

**Step 7: getProduct(4)**

Only three numbers have been added since the latest zero.

The requested range includes zero.

Result: `0`

**Step 8: Add 8**

```text
Stream:          [3, 0, 2, 5, 4, 8]
Prefix products: [1, 2, 10, 40, 320]
```

**Step 9: getProduct(2)**

\[
\frac{320}{10}=32
\]

Result: `32`

## Complexity Analysis

Let `n` represent the number of non-zero values added since the most recent zero.

| Operation | Time Complexity | Explanation |
|---|---|---|
| Constructor | `O(1)` | Initializes a one-element array. |
| `add(num)` | `O(1)` | Appends a cumulative product or resets the array. |
| `getProduct(k)` | `O(1)` | Uses a boundary check and one division. |

**Auxiliary Space:** `O(n)`

The prefix array stores cumulative products only for values added after the latest zero.

## Edge Cases

| Number stream | Query | Expected result | Explanation |
|---|---|---:|---|
| `[5]` | `getProduct(1)` | `5` | Single-element query |
| `[3, 2, 4]` | `getProduct(2)` | `8` | Product of the last two numbers |
| `[3, 0, 5]` | `getProduct(1)` | `5` | Query occurs after zero |
| `[3, 0, 5]` | `getProduct(2)` | `0` | Requested range includes zero |
| `[0, 0, 7]` | `getProduct(2)` | `0` | Requested range includes zero |
| `[2, 3, 4]` | `getProduct(3)` | `24` | Entire non-zero sequence |

## Key Takeaways

1. **Prefix Products:** Convert repeated range multiplication into constant-time division.
2. **Zero Handling:** Reset cumulative products whenever zero is encountered.
3. **Sentinel Values:** Initializing the prefix array with `1` simplifies indexing and calculations.
4. **Boundary Checks:** Determine whether a requested range includes a zero by comparing `k` with the available prefix history.
5. **Data Structure Design:** Performing calculations during insertion makes retrieval efficient.
6. **JavaScript Precision:** The problem guarantees that contiguous products fit in a 32-bit integer, keeping the relevant products within JavaScript's exact integer range.

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── JavaScript/
        └── 1352_Product_of_the_Last_K_Numbers.js
```

## References

- [LeetCode 1352 — Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/)
- [Prefix Sum and Prefix Product Techniques](https://en.wikipedia.org/wiki/Prefix_sum)

---

**Solution Status:** Completed

**Primary Approach:** Prefix Products with Zero Reset

**Language:** JavaScript

**Time Complexity:** `O(1)` per operation

**Auxiliary Space Complexity:** `O(n)`

**Key Concepts:** Prefix Products, Data Structure Design, Zero Handling, Arrays, Constant-Time Queries