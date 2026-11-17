
/**
 * LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
 *
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minimumChanges = function(s, k) {
    const n = s.length;
    const INF = Infinity;

    // Precompute all proper divisors for possible substring lengths.
    const divisors = Array.from({ length: n + 1 }, () => []);

    for (let d = 1; d < n; d++) {
        for (let len = d * 2; len <= n; len += d) {
            divisors[len].push(d);
        }
    }

    // cost[i][j] = minimum changes to make s[i...j]
    // a semi-palindrome.
    const cost = Array.from(
        { length: n },
        () => Array(n).fill(INF)
    );

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const len = j - i + 1;

            for (const d of divisors[len]) {
                let changes = 0;

                // Compare corresponding positions in each
                // modulo-d group from opposite ends.
                for (let offset = 0; offset < d; offset++) {
                    let left = i + offset;
                    let right = j - d + 1 + offset;

                    while (left < right) {
                        if (s[left] !== s[right]) {
                            changes++;
                        }

                        left += d;
                        right -= d;
                    }
                }

                cost[i][j] = Math.min(
                    cost[i][j],
                    changes
                );
            }
        }
    }

    // dp[p][i] = minimum changes to partition the first i
    // characters into exactly p semi-palindromes.
    const dp = Array.from(
        { length: k + 1 },
        () => Array(n + 1).fill(INF)
    );

    dp[0][0] = 0;

    for (let p = 1; p <= k; p++) {
        // Each substring must contain at least 2 characters.
        const minEnd = p * 2;
        const maxEnd = n - (k - p) * 2;

        for (let i = minEnd; i <= maxEnd; i++) {
            // The final substring is s[j...i-1].
            // It must have a length of at least 2.
            for (let j = (p - 1) * 2; j <= i - 2; j++) {
                if (dp[p - 1][j] === INF) {
                    continue;
                }

                dp[p][i] = Math.min(
                    dp[p][i],
                    dp[p - 1][j] + cost[j][i - 1]
                );
            }
        }
    }

    return dp[k][n];
};
