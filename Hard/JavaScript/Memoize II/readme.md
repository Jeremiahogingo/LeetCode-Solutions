# LeetCode 2630: Memoize II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Memoization-blue)

## Problem Description

Implement a `memoize` function that caches the results of calls to another function, `fn`.

When the returned function is called with arguments that have already been used, it should return the cached result instead of executing `fn` again.

Unlike basic memoization, this problem requires handling different argument types, including objects and functions, while respecting reference identity.

**Problem link:** [LeetCode 2630 — Memoize II](https://leetcode.com/problems/memoize-ii/description/)

## Approach: Nested Maps

Use a hierarchy of `Map` objects to represent each sequence of arguments.

1. Start at the root cache.
2. For each argument, find or create a child `Map` keyed by that argument.
3. After processing all arguments, check whether the current node contains a cached result.
4. If the result exists, return it without executing `fn`.
5. Otherwise, execute `fn`, store its result, and return it.

A unique `Symbol` identifies cached results, allowing the cache to distinguish a stored `undefined` result from a missing entry.

## JavaScript Solution

```javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    const RESULT = Symbol("result");

    return function (...args) {
        let node = cache;

        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }

            node = node.get(arg);
        }

        if (node.has(RESULT)) {
            return node.get(RESULT);
        }

        const result = fn.apply(this, args);
        node.set(RESULT, result);

        return result;
    };
}
```

## Example

```javascript
let calls = 0;

const fn = (a, b) => {
    calls++;
    return a + b;
};

const memoizedFn = memoize(fn);

memoizedFn(2, 3); // 5 — executes fn
memoizedFn(2, 3); // 5 — returns cached result

console.log(calls); // 1
```

The second call uses the same argument sequence, so the original function is not executed again.

## Complexity Analysis

Let \(k\) be the number of arguments in a function call.

- **Time Complexity:** \(O(k)\) per call, excluding the execution time of `fn`.
- **Space Complexity:** Depends on the number of distinct argument sequences and their lengths stored in the cache.

## Key Takeaways

- Memoization avoids repeated computation by caching function results.
- Nested `Map` objects represent argument sequences without serializing them.
- JavaScript `Map` keys distinguish objects by reference identity.
- Using `has()` allows cached values such as `undefined` to be distinguished from missing entries.
- `fn.apply(this, args)` preserves the calling context of the wrapped function.

## References

- [LeetCode 2630 — Memoize II](https://leetcode.com/problems/memoize-ii/description/)
- [MDN: Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN: Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
