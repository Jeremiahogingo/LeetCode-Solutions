# 1606. Find Servers That Handled Most Number of Requests

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Topic-Heap%20%7C%20Fenwick%20Tree-purple)
![LeetCode](https://img.shields.io/badge/LeetCode-1606-yellow)

## Problem

**[Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/)**

You are given:

- An integer `k`, representing the number of servers numbered from `0` to `k - 1`.
- An array `arrival`, where `arrival[i]` represents the arrival time of the ith request.
- An array `load`, where `load[i]` represents the time required to process the ith request.

Requests are assigned according to the following rules:

1. Request `i` first attempts to use server `i % k`.
2. If that server is busy, the request searches for the next available server in circular order.
3. If no server is available, the request is dropped.
4. A server becomes available when its previous request finishes.

Return the IDs of all servers that handled the maximum number of requests, in ascending order.

## Approach: Min-Heap + Fenwick Tree

A combination of a Min-Heap and a Fenwick Tree efficiently manages server availability and request assignments.

### 1. Min-Heap — Track Busy Servers

The Min-Heap stores pairs of:

```python
(finish_time, server_id)
```

It allows us to efficiently identify the server whose current request finishes earliest.

When a new request arrives:

- Check the earliest finishing request.
- Release its server if `finish_time <= arrival_time`.
- Continue releasing servers until the earliest finishing request is still in progress.

The comparison must use `<=` because a server finishing exactly when a request arrives is already available.

### 2. Fenwick Tree — Track Available Servers

A Fenwick Tree (Binary Indexed Tree) maintains the availability status of every server.

Each server has a value:

- `1` means the server is available.
- `0` means the server is busy.

The tree supports three important operations:

| Operation | Purpose | Complexity |
|---|---|---|
| `add()` | Update server availability | O(log k) |
| `prefix_sum()` | Count available servers in a range | O(log k) |
| `find_kth()` | Find the server at a given availability rank | O(log k) |

This avoids scanning every server to find the next available one.

## Solution

```python
import heapq
from typing import List


class FenwickTree:
    def __init__(self, n: int):
        self.n = n

        # Initially, every server is available.
        self.tree = [0] + [
            i & -i for i in range(1, n + 1)
        ]

    def add(self, index: int, delta: int) -> None:
        """Update the availability count at an index."""
        i = index + 1

        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, end: int) -> int:
        """Count available servers in [0, end)."""
        total = 0
        i = end

        while i > 0:
            total += self.tree[i]
            i -= i & -i

        return total

    def find_kth(self, rank: int) -> int:
        """Find the zero-based index of the kth available server."""
        index = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = index + step

            if nxt <= self.n and self.tree[nxt] < rank:
                index = nxt
                rank -= self.tree[nxt]

            step >>= 1

        return index


class Solution:
    def busiestServers(
        self,
        k: int,
        arrival: List[int],
        load: List[int]
    ) -> List[int]:

        available = FenwickTree(k)
        busy = []

        request_count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            # 1. Release servers whose requests have finished.
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                available.add(server, 1)

            # 2. Check whether any server is available.
            total_available = available.prefix_sum(k)

            if total_available == 0:
                continue

            # 3. Find the preferred server.
            preferred = i % k

            # Count available servers before the preferred ID.
            before_preferred = available.prefix_sum(preferred)

            # 4. Find the next available server, wrapping if needed.
            if total_available > before_preferred:
                rank = before_preferred + 1
            else:
                rank = 1

            server = available.find_kth(rank)

            # 5. Mark the selected server as busy.
            available.add(server, -1)

            heapq.heappush(
                busy,
                (start + duration, server)
            )

            # 6. Record the successfully handled request.
            request_count[server] += 1

        # 7. Return all servers with the maximum request count.
        max_requests = max(request_count)

        return [
            server
            for server, count in enumerate(request_count)
            if count == max_requests
        ]
```

## Example and Dry Run

**Input:**

```python
k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]
```

**Request assignment:**

| Request | Arrival | Preferred Server | Assigned Server | Explanation |
|---:|---:|---:|---:|---|
| 0 | 1 | 0 | 0 | All servers are available |
| 1 | 2 | 1 | 1 | Server 1 is available |
| 2 | 3 | 2 | 2 | Server 2 is available |
| 3 | 4 | 0 | 1 | Server 0 is busy; server 1 has finished |
| 4 | 5 | 1 | Dropped | All servers are busy |

**Final request counts:**

| Server | Requests Handled |
|---:|---:|
| 0 | 1 |
| 1 | 2 |
| 2 | 1 |

**Output:**

```python
[1]
```

**Explanation:**

Server `1` handled two requests, while servers `0` and `2` each handled one request. Therefore, server `1` is the busiest server.

## Understanding Circular Server Selection

Suppose:

```python
k = 5
preferred = 2
available_servers = [0, 3, 4]
```

The algorithm searches for the first available server starting from server `2`.

- Server `2` is busy.
- Server `3` is available.
- Server `3` is selected.

Now consider:

```python
available_servers = [0, 1]
preferred = 3
```

No available server exists at or after server `3`, so the search wraps around and selects server `0`.

The Fenwick Tree makes both operations efficient by using prefix sums and rank-based selection.

## Complexity Analysis

Let:

- `k` represent the number of servers.
- `n` represent the number of requests.

| Operation | Time Complexity |
|---|---|
| Initialize Fenwick Tree | O(k) |
| Process each request | O(log k) |
| Release completed servers | O(log k) per released server |
| Find next available server | O(log k) |
| Update server availability | O(log k) |

**Overall Time Complexity:**

\[
O(k+n\log k)
\]

Each accepted request enters the heap once and can be removed once. Therefore, the total number of heap insertions and removals is bounded by the number of requests.

**Space Complexity:**

\[
O(k)
\]

The Fenwick Tree, request-count array, and busy-server heap require at most O(k) space because no more than `k` servers can be busy simultaneously.

## Important Edge Cases

| Scenario | Expected Behavior |
|---|---|
| Only one server (`k = 1`) | Every request is handled whenever the server is free |
| All servers are busy | Drop the incoming request |
| Preferred server is busy | Select the next available server |
| No available server after preferred ID | Wrap around to server `0` |
| Server finishes exactly at arrival time | Release and reuse the server |
| Multiple servers share the maximum count | Return all of them |
| No requests are successfully handled | Return all server IDs because every server has zero requests |

## Key Takeaways

- A Min-Heap efficiently tracks server completion times.
- Fenwick Trees support efficient updates and prefix-sum queries.
- Order-statistic queries help find the next available server without linear scanning.
- Modular arithmetic (`i % k`) determines the preferred server.
- Circular searching can be implemented using prefix counts and rank-based selection.
- Combining suitable data structures can improve the performance of simulation problems.

## Related Problems

- [LeetCode 1267 – Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)
- [LeetCode 621 – Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [LeetCode 1845 – Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/)
- [LeetCode 1851 – Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

## Repository Structure

```text
LeetCode-Solutions/
└── Hard/
    └── Python/
        ├── 1606_Find_Servers_That_Handled_Most_Number_of_Requests.py
        └── README.md
```

## References

- [LeetCode – Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)
- [Fenwick Tree – CP-Algorithms](https://cp-algorithms.com/data_structures/fenwick.html)
- [Python Documentation – heapq](https://docs.python.org/3/library/heapq.html)

---

**Problem:** 1606  
**Difficulty:** Hard  
**Language:** Python  
**Topics:** Array, Heap, Simulation, Fenwick Tree, Binary Indexed Tree, Order Statistics