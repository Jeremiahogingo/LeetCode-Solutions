# LeetCode 2623: Memoize

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Memoization-blue)

## Problem Description

Given a function `fn`, return a memoized version of that function.

A memoized function stores the results of previous calls and returns the cached value when called again with the same arguments, avoiding redundant executions.

The problem uses three possible functions: `sum`, `fib`, and `factorial`. Argument order matters, so calls with `(2, 3)` and `(3, 2)` must be cached separately.

**Problem link:** [LeetCode 2623 — Memoize](https://leetcode.com/problems/memoize/description/)

## Approach: Hash Map Caching

Use a JavaScript `Map` to store computed results, with the serialized argument list as the cache key.

1. Create an empty cache.
2. Serialize the arguments using `JSON.stringify(args)` to generate a key.
3. If the key exists in the cache, return its stored result.
4. Otherwise, execute the original function with the supplied arguments.
5. Store the result in the cache and return it.

Using `cache.has(key)` correctly distinguishes a missing entry from a cached result such as `undefined`.

## JavaScript Solution

```javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();

    return function (...args) {
        const key = JSON.stringify(args);

        if (cache.has(key)) {
            return cache.get(key);
        }

        const result = fn.apply(this, args);
        cache.set(key, result);

        return result;
    };
}
```

## Example

```javascript
let callCount = 0;

const sum = (a, b) => {
    callCount++;
    return a + b;
};

const memoizedSum = memoize(sum);

memoizedSum(2, 3); // 5 — executes sum
memoizedSum(2, 3); // 5 — returns cached result
memoizedSum(3, 2); // 5 — executes sum again

console.log(callCount); // 2
```

The first call computes and caches the result. The second call reuses the cached value, while the third call uses a different argument order and therefore has a different cache key.

## Complexity Analysis

Let \(k\) be the number of arguments and \(u\) the number of distinct argument combinations cached.

- **Time Complexity:** \(O(k)\) caching overhead per call, excluding the execution time of `fn`. This accounts for serializing the arguments.
- **Space Complexity:** \(O(u)\) cache entries, with additional storage proportional to the total size of the serialized argument keys and cached results.

For this problem's numeric arguments, key generation and cache lookup are efficient.

## Key Takeaways

- Memoization avoids repeated calculations by storing previously computed results.
- A cache key must represent the complete argument sequence.
- Argument order matters when identifying repeated calls.
- `Map.has()` safely checks for cached entries even when the result is `undefined`.
- Memoization is particularly useful for recursive computations such as Fibonacci numbers.

## Repository Structure

```text
Memoize/
├── solution.js
└── README.md
```

## References

- [LeetCode Problem 2623](https://leetcode.com/problems/memoize/description/)
- [MDN: JavaScript Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN: JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
