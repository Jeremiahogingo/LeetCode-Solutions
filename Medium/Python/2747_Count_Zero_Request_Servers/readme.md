# LeetCode 2747: Count Zero Request Servers

## Problem Description

Given `n` servers, a list of request logs, an integer `x`, and an array of queries, determine how many servers received no requests during the time interval associated with each query.

Each log entry is represented as:

```
[server_id, time]
```

For every query `q`, consider the inclusive time interval:

\\[ [q-x,\ q] \\]

Return an array where each element represents the number of servers that received no requests during the corresponding query interval.

Problem link: [LeetCode 2747 — Count Zero Request Servers](https://leetcode.com/problems/count-zero-request-servers/description/?utm_source=chatgpt.com)

## Approach: Sorting and Sliding Window

Use an offline query-processing technique with sorting, two pointers, and a frequency array.

Instead of checking every log for every query, sort the logs and process queries chronologically while maintaining the servers with requests inside the current time window.

### Algorithm

1. Sort `logs` by request time.
2. Sort the queries by time while preserving their original indices.
3. Initialize two pointers, `left` and `right`, to maintain the current window.
4. Use a frequency array to track the number of requests received by each server within the window.
5. Move `right` forward to include logs with timestamps less than or equal to the current query time.
6. Move `left` forward to remove logs with timestamps strictly less than `query_time - x`.
7. Track the number of distinct servers with active requests.
8. Calculate the number of servers without requests by subtracting the active server count from `n`.
9. Store each answer at its original query index and return the result.

The inclusive interval boundaries are important: requests at `query_time - x` and `query_time` must both be included.

## Python Solution

```
from typing import List

class Solution:
    def countServers(
        self,
        n: int,
        logs: List[List[int]],
        x: int,
        queries: List[int]
    ) -> List[int]:

        # Sort logs by request time.
        logs.sort(key=lambda log: log[1])

        # Process queries in chronological order.
        sorted_queries = sorted(
            (time, index)
            for index, time in enumerate(queries)
        )

        # Track the number of requests per server.
        counts = [0] * (n + 1)

        left = right = 0
        active_servers = 0

        result = [0] * len(queries)

        for query_time, index in sorted_queries:
            start_time = query_time - x

            # Include requests up to the query time.
            while right < len(logs) and logs[right][1] <= query_time:
                server_id = logs[right][0]

                if counts[server_id] == 0:
                    active_servers += 1

                counts[server_id] += 1
                right += 1

            # Remove requests outside the current window.
            while left < right and logs[left][1] < start_time:
                server_id = logs[left][0]

                counts[server_id] -= 1

                if counts[server_id] == 0:
                    active_servers -= 1

                left += 1

            # Count servers without requests.
            result[index] = n - active_servers

        return result
```

## Examples

Example 1

Input:

```
n = 3
logs = [[1,3], [2,6], [1,5]]
x = 5
queries = [10,11]
```

Output:

```
[1,2]
```

Explanation:

For query `10`:

```
Time window: [5, 10]

Active servers: {1, 2}
Zero-request servers: 3 - 2 = 1
```

For query `11`:

```
Time window: [6, 11]

Active servers: {2}
Zero-request servers: 3 - 1 = 2
```

Example 2

Input:

```
n = 3
logs = [[2,4], [2,1], [1,2], [3,1]]
x = 2
queries = [3,4]
```

Output:

```
[0,1]
```

Explanation:

- Query `3` considers `[1,3]`. All three servers received requests, so the answer is `0`.
- Query `4` considers `[2,4]`. Only servers `1` and `2` received requests, so the answer is `1`.

## Complexity Analysis

Let:

- \\(n\\) = number of servers.
- \\(L\\) = number of request logs.
- \\(Q\\) = number of queries.

| Operation                 | Complexity                   |
| ------------------------- | ---------------------------- |
| Sort request logs         | \\(O(L\log L)\\)             |
| Sort queries              | \\(O(Q\log Q)\\)             |
| Sliding window processing | \\(O(L+Q)\\)                 |
| Total time                | \\(O(L\log L+Q\log Q+L+Q)\\) |

Auxiliary Space Complexity: \\(O(n+L+Q)\\), including the server frequency array, sorted query pairs, result array, and sorting workspace.

Each log enters and leaves the sliding window at most once.

## Key Takeaways

- Sorting allows queries to be processed chronologically.
- Sliding windows avoid repeatedly scanning the entire log collection.
- Two pointers efficiently maintain the current time interval.
- A frequency array tracks multiple requests from the same server.
- Count distinct active servers rather than individual requests.
- Inclusive time boundaries require removing logs with `time < query_time - x`, not `<=`.
- Original query indices preserve the expected output order.

## Related Problems

These problems reinforce sliding windows, sorting, frequency counting, and efficient range queries.

| Problem                                                                                                                                                                                                              | Difficulty | Connection                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------ |
| [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/?utm_source=chatgpt.com)                                                                                                            | Easy       | Sliding window and hash tables       |
| [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/?utm_source=chatgpt.com)                                                                                                          | Hard       | Ordered sliding window               |
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/?utm_source=chatgpt.com)                                                                                                          | Hard       | Efficient sliding window maintenance |
| [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/?utm_source=chatgpt.com) | Medium     | Sliding window with maintained state |
| [2563. Count the Number of Fair Pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/?utm_source=chatgpt.com)                                                                                         | Medium     | Sorting and two pointers             |

## Repository Structure

```
LeetCode-Solutions/
└── Medium/
    └── Python/
        └── 2747_Count_Zero_Request_Servers.py
```

## References

- [LeetCode Problem 2747](https://leetcode.com/problems/count-zero-request-servers/?utm_source=chatgpt.com)
- [Python Sorting Documentation](https://docs.python.org/3/howto/sorting.html?utm_source=chatgpt.com)
- [Python List Documentation](https://docs.python.org/3/tutorial/introduction.html?utm_source=chatgpt.com#lists)
