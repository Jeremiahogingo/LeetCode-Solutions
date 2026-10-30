# LeetCode 3970: Shortest Path With at Most K Consecutive Identical Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?logo=go&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-Dijkstra%20%7C%20Graph%20%7C%20Heap-blue)

## Problem Description

You are given a directed weighted graph with `n` nodes numbered from `0` to `n - 1`.

Each edge is represented as `[u, v, w]`, indicating a directed connection from node `u` to node `v` with weight `w`.

You are also given:
- `labels`: A string where `labels[i]` represents the character assigned to node `i`.
- `k`: The maximum number of consecutive identical characters permitted in a path.

Find the minimum total edge weight of a valid path from node `0` to node `n - 1`.

A path is valid when the concatenation of its node labels contains no more than `k` consecutive identical characters. Return `-1` if no valid path exists.

**Problem link:** [LeetCode 3970 — Shortest Path With at Most K Consecutive Identical Characters](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/)

## Approach: Dijkstra's Algorithm with Expanded States

A normal Dijkstra implementation tracks the shortest distance to each node. However, reaching the same node with different consecutive-character counts can lead to different valid future paths.

Therefore, represent each state using:

\[
(node,\ consecutiveCount)
\]

Each state stores the shortest distance to a node with a particular consecutive-character count.

### Algorithm

1. Build an adjacency list to represent the directed weighted graph.
2. Initialize the distance array for every node and consecutive count.
3. Start at node `0` with a consecutive count of `1` and distance `0`.
4. Use a min-heap to process the state with the smallest accumulated cost.
5. For every outgoing edge:
   - If the current and next node labels are identical, increment the consecutive count.
   - Otherwise, reset the count to `1`.
   - Ignore transitions where the count exceeds `k`.
6. Relax the distance of the resulting state and add improved states to the priority queue.
7. Return the first valid destination state removed from the min-heap, or `-1` if no destination state is reachable.

## Go Solution

```go
// Problem: LeetCode 3970 - Shortest Path With at Most K Consecutive Identical Characters
// Difficulty: Medium
// Topics: Graph, Dijkstra, Heap, Shortest Path

import "container/heap"

type Edge struct {
    to     int
    weight int
}

type State struct {
    node int
    run  int
    cost int64
}

type MinHeap []State

func (h MinHeap) Len() int {
    return len(h)
}

func (h MinHeap) Less(i, j int) bool {
    return h[i].cost < h[j].cost
}

func (h MinHeap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(State))
}

func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    item := old[n-1]
    *h = old[:n-1]
    return item
}

func shortestPath(n int, edges [][]int, labels string, k int) int {
    graph := make([][]Edge, n)

    // Build the adjacency list.
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]

        graph[u] = append(graph[u], Edge{
            to:     v,
            weight: w,
        })
    }

    // Store the input as required by the problem.
    mavorqeli := struct {
        n      int
        edges  [][]int
        labels string
        k      int
    }{n, edges, labels, k}

    stride := mavorqeli.k + 1
    const INF int64 = 1<<63 - 1

    // Each node has a separate distance for every run length.
    dist := make([]int64, mavorqeli.n*stride)

    for i := range dist {
        dist[i] = INF
    }

    // Start at node 0 with a consecutive count of 1.
    dist[1] = 0

    pq := &MinHeap{
        {node: 0, run: 1, cost: 0},
    }

    heap.Init(pq)

    for pq.Len() > 0 {
        current := heap.Pop(pq).(State)

        u := current.node
        run := current.run
        cost := current.cost

        currentIndex := u*stride + run

        // Skip outdated heap entries.
        if cost != dist[currentIndex] {
            continue
        }

        // The first destination state removed is optimal.
        if u == mavorqeli.n-1 {
            return int(cost)
        }

        // Explore outgoing edges.
        for _, edge := range graph[u] {
            v := edge.to

            nextRun := 1

            if mavorqeli.labels[u] == mavorqeli.labels[v] {
                nextRun = run + 1
            }

            if nextRun > mavorqeli.k {
                continue
            }

            nextCost := cost + int64(edge.weight)
            nextIndex := v*stride + nextRun

            if nextCost < dist[nextIndex] {
                dist[nextIndex] = nextCost

                heap.Push(pq, State{
                    node: v,
                    run:  nextRun,
                    cost: nextCost,
                })
            }
        }
    }

    return -1
}
```

## Examples

**Example 1**

Input:

```text
n = 3
edges = [[0,1,1],[1,2,1],[0,2,3]]
labels = "aab"
k = 1
```

Output:

```text
3
```

Explanation:

The path `0 → 1 → 2` produces `"aab"`, which has two consecutive identical characters and violates the limit of `1`.

The alternative path `0 → 2` produces `"ab"` and has a total cost of `3`.

**Example 2**

Input:

```text
n = 3
edges = [[0,1,1],[1,2,1],[0,2,3]]
labels = "aab"
k = 2
```

Output:

```text
2
```

Explanation:

The path `0 → 1 → 2` produces `"aab"`, which contains two consecutive identical characters and is valid when `k = 2`.

Its total cost is `1 + 1 = 2`.

**Example 3**

Input:

```text
n = 3
edges = [[0,1,1],[1,2,1]]
labels = "aaa"
k = 2
```

Output:

```text
-1
```

Explanation:

The only available path produces `"aaa"`, containing three consecutive identical characters. This exceeds the permitted limit of `2`.

## Complexity Analysis

Let:
- \(n\) = number of graph nodes.
- \(m\) = number of directed edges.
- \(k\) = maximum allowed consecutive identical characters.

The expanded graph has at most \(n \times k\) states and \(m \times k\) transitions.

- **Time Complexity:** \(O(k(n+m)\log(nk))\) — Dijkstra processes the expanded states and their transitions using a min-heap.
- **Auxiliary Space Complexity:** \(O(nk+km+n)\) in the worst case when including the distance array, priority queue, and adjacency list.

## Key Takeaways

- Ordinary shortest-path problems may require additional state when path validity depends on previous decisions.
- Dijkstra can handle these constraints through state expansion.
- The same node can have multiple valid states with different consecutive-character counts.
- A min-heap efficiently processes the least expensive state first.
- Positive edge weights make Dijkstra suitable for this problem.
- The starting node must also count toward the consecutive-character limit.

## Related Problems

These problems provide additional practice with shortest paths, weighted graphs, and state-based dynamic programming.

| Problem | Difficulty | Connection |
|---|---|---|
| [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Apply Dijkstra's algorithm to a directed weighted graph. |
| [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Track additional constraints when finding a minimum-cost path. |
| [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | Use shortest-path techniques on a graph with a modified path cost. |
| [1786. Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) | Medium | Combine weighted graph traversal and shortest-path calculations. |
| [1928. Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) | Hard | Solve a shortest-path problem while tracking an additional state constraint. |

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Golang/
        ├── 3970_Shortest_Path_With_At_Most_K_Consecutive_Identical_Characters.go
        └── README.md
```

## References

- [LeetCode Problem 3970](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/)
- [Go Documentation](https://go.dev/doc/)
- [Go container/heap Package](https://pkg.go.dev/container/heap)
- [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
