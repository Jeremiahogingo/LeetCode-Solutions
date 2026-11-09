
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
