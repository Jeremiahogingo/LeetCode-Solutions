# 2621. Sleep

![LeetCode](https://img.shields.io/badge/LeetCode-2621-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow?logo=javascript)
![Topic](https://img.shields.io/badge/Topic-Asynchronous%20Programming-blue)

## Problem Overview

Implement an asynchronous function `sleep(millis)` that returns a Promise which resolves after approximately `millis` milliseconds.

The delay must be non-blocking, allowing JavaScript to continue executing other tasks while waiting. Minor deviations from the requested duration are acceptable. <Cite refs={["turn765850search1","turn765850search0"]}/>

**LeetCode:** [Sleep](https://leetcode.com/problems/sleep/description/)

## Approach: Promise + setTimeout

JavaScript's `setTimeout()` schedules a callback to execute after a specified delay, but it does not directly return a Promise. Wrapping it in a Promise makes the delay awaitable.

### Algorithm

1. Create a new Promise.
2. Pass its `resolve` function to `setTimeout`.
3. Schedule the timer for `millis` milliseconds.
4. When the timer fires, `resolve` is called and the Promise fulfills.
5. The caller can continue using `.then()` or `await`.

## JavaScript Implementation

```javascript
/**
 * @param {number} millis
 * @return {Promise}
 */
var sleep = async function (millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
};
```

## Example Walkthrough

**Input:**

```javascript
millis = 100;
```

**Usage:**

```javascript
let start = Date.now();

sleep(100).then(() => {
    console.log(Date.now() - start);
});
```

**Expected output:**

```text
Approximately 100
```

### Execution Flow

```text
sleep(100) called
       |
       v
Promise created
       |
       v
setTimeout schedules resolve after 100 ms
       |
       v
JavaScript continues other work
       |
       v
Timer callback executes
       |
       v
Promise resolves
       |
       v
.then() callback or awaiting code continues
```

The elapsed time may be slightly greater than 100 milliseconds because timer execution depends on event-loop scheduling.

## Edge Cases

| Input | Expected Behavior | Explanation |
|---|---|---|
| `1` | Resolves after approximately 1 ms | Minimum permitted delay |
| `100` | Resolves after approximately 100 ms | Standard delay |
| `500` | Resolves after approximately 500 ms | Longer delay |
| `1000` | Resolves after approximately 1000 ms | Maximum permitted delay |

The problem guarantees that `millis` is between `1` and `1000`, inclusive, so additional input validation is unnecessary.

## Complexity Analysis

- **Time Complexity:** \(O(1)\) for creating the Promise and scheduling the timer, excluding the elapsed waiting time.
- **Auxiliary Space Complexity:** \(O(1)\) — only a Promise, timer, and callback reference are needed.

## Key Takeaways

- `setTimeout()` schedules a callback without blocking the JavaScript thread.
- A Promise allows asynchronous operations to be awaited.
- Calling `resolve` fulfills a Promise and allows dependent asynchronous code to continue.
- `async` functions automatically return Promises.
- Timers specify a minimum scheduling delay, not a guarantee of execution at an exact millisecond.

## Related Problems

- [Promise Time Limit](https://leetcode.com/problems/promise-time-limit/)
- [Add Two Promises](https://leetcode.com/problems/add-two-promises/)
- [Sleep](https://leetcode.com/problems/sleep/description/)

## References

- [LeetCode #2621 — Sleep](https://leetcode.com/problems/sleep/description/)
- [MDN — `setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)
- [MDN — Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*