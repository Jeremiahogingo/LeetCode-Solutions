
/**
 * LeetCode 44 - Wildcard Matching
 *
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const m = s.length;
    const n = p.length;

    // dp[j] indicates whether the current prefix of s
    // matches the first j characters of p.
    const dp = Array(n + 1).fill(false);

    // Two empty strings match.
    dp[0] = true;

    // Leading '*' characters can match an empty string.
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[j] = dp[j - 1];
        } else {
            break;
        }
    }

    // Process each character in s.
    for (let i = 1; i <= m; i++) {
        // Previous row's first column is always false
        // because a non-empty string cannot match an empty pattern.
        let diagonal = dp[0];
        dp[0] = false;

        for (let j = 1; j <= n; j++) {
            // Preserve the previous row's value before overwriting.
            const previous = dp[j];

            if (p[j - 1] === '*') {
                // '*' matches either:
                // 1. An empty sequence: dp[j - 1]
                // 2. One additional character: previous
                dp[j] = dp[j - 1] || previous;
            } else {
                // '?' matches any single character.
                // A normal character must match exactly.
                dp[j] =
                    diagonal &&
                    (p[j - 1] === '?' || p[j - 1] === s[i - 1]);
            }

            // Update the diagonal for the next iteration.
            diagonal = previous;
        }
    }

    return dp[n];
};
