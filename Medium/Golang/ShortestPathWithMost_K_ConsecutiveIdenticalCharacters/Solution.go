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
	// Build the directed weighted graph.
	graph := make([][]Edge, n)

	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		graph[u] = append(graph[u], Edge{
			to:     v,
			weight: w,
		})
	}

	// Each state is represented by (node, consecutive count).
	stride := k + 1
	const INF int64 = 1<<63 - 1

	dist := make([]int64, n*stride)

	for i := range dist {
		dist[i] = INF
	}

	// Starting node already contributes one character.
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

		// Ignore outdated priority queue entries.
		if cost != dist[currentIndex] {
			continue
		}

		// The first destination state removed is optimal.
		if u == n-1 {
			return int(cost)
		}

		// Explore outgoing edges.
		for _, edge := range graph[u] {
			v := edge.to

			nextRun := 1

			if labels[u] == labels[v] {
				nextRun = run + 1
			}

			// Reject paths exceeding the consecutive limit.
			if nextRun > k {
				continue
			}

			nextCost := cost + int64(edge.weight)
			nextIndex := v*stride + nextRun

			// Relax the expanded state.
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