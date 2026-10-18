# 🦘 Jump Game

![LeetCode](https://img.shields.io/badge/LeetCode-55-orange?style=flat-square&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?style=flat-square&logo=go)
![Time](https://img.shields.io/badge/Time-O(n)-blue?style=flat-square)
![Space](https://img.shields.io/badge/Space-O(1)-blue?style=flat-square)

## Overview

Given an integer array `nums`, each element represents the maximum jump length from that position.

Return `true` if you can reach the last index from the first index; otherwise, return `false`.

### Example

```text
Input:  nums = [2,3,1,1,4]
Output: true

Input:  nums = [3,2,1,0,4]
Output: false
```

## Approach

Use a **greedy algorithm** to track the farthest reachable index.

1. Initialize `farthest = 0`.
2. Iterate through the array.
3. If `i > farthest`, the current index cannot be reached, so return `false`.
4. Update `farthest` to `max(farthest, i + nums[i])`.
5. Return `true` once the last index is reachable.

This avoids exploring every possible jump.

## Implementation

```go
func canJump(nums []int) bool {
    farthest := 0

    for i, jump := range nums {
        if i > farthest {
            return false
        }

        if i+jump > farthest {
            farthest = i + jump
        }

        if farthest >= len(nums)-1 {
            return true
        }
    }

    return true
}
```

## Example Walkthrough

For `nums = [2,3,1,1,4]`:

| Index | Jump length | Farthest reachable |
|---:|---:|---:|
| 0 | 2 | 2 |
| 1 | 3 | 4 |
| 2 | 1 | 4 |
| 3 | 1 | 4 |

At index `1`, the farthest reachable position becomes `4`, which is the last index.

**Output:** `true`

For `nums = [3,2,1,0,4]`, the farthest reachable position stops at index `3`. Since index `4` cannot be reached, the output is `false`.

## Edge Cases

| Case | Input | Output | Behavior |
|---|---|---|---|
| Single element | `[0]` | `true` | Already at the destination |
| Cannot move | `[0,1]` | `false` | The second index is unreachable |
| Jump directly to end | `[2,0,0]` | `true` | The destination is reachable |
| Zero blocks progress | `[3,2,1,0,4]` | `false` | Reachability stops before the end |
| Multiple possible paths | `[2,3,1,1,4]` | `true` | A reachable position extends the range |

## Complexity

Let \(n\) be the length of `nums`.

| Metric | Complexity |
|---|---|
| Time | **O(n)** |
| Auxiliary space | **O(1)** |

Each index is processed at most once, and the algorithm uses only a constant amount of additional memory.

## Key Takeaways

- Greedy reachability eliminates unnecessary path exploration.
- `farthest` represents the maximum index reachable so far.
- If `i > farthest`, the destination cannot be reached.
- The algorithm runs in linear time with constant auxiliary space.

## Related Problems

- [#45 — Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [#134 — Gas Station](https://leetcode.com/problems/gas-station/)
- [#1024 — Video Stitching](https://leetcode.com/problems/video-stitching/)

## Reference

[LeetCode — Jump Game](https://leetcode.com/problems/jump-game/)

---

<div align="center">

**Track Reachability → Extend the Range → Reach the End**

</div>