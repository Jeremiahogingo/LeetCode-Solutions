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

        # Count active requests for each server.
        counts = [0] * (n + 1)

        left = right = 0
        active_servers = 0

        result = [0] * len(queries)

        for query_time, index in sorted_queries:
            start_time = query_time - x

            # Add requests that fall before or at the
            # current query's right boundary.
            while right < len(logs) and logs[right][1] <= query_time:
                server_id = logs[right][0]

                if counts[server_id] == 0:
                    active_servers += 1

                counts[server_id] += 1
                right += 1

            # Remove requests outside the left boundary.
            while left < right and logs[left][1] < start_time:
                server_id = logs[left][0]

                counts[server_id] -= 1

                if counts[server_id] == 0:
                    active_servers -= 1

                left += 1

            # Servers without requests in the current window.
            result[index] = n - active_servers

        return result