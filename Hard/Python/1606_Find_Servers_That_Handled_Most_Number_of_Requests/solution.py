import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))   # min-heap of extended indices
        busy = []                   # (finish_time, server_id)
        count = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            # Free finished servers, re-insert with extended index
            while busy and busy[0][0] <= t:
                _, srv = heapq.heappop(busy)
                heapq.heappush(available, i + (srv - i) % k)

            if available:
                extended = heapq.heappop(available)
                srv = extended % k
                heapq.heappush(busy, (t + l, srv))
                count[srv] += 1

        max_handled = max(count)
        return [i for i, c in enumerate(count) if c == max_handled]