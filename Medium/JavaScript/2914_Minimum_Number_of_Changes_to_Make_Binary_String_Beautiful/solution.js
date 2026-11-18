
/**
 * LeetCode 2914 - Minimum Number of Changes
 * to Make Binary String Beautiful
 *
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    let changes = 0;

    // Process the string in non-overlapping pairs.
    for (let i = 0; i < s.length; i += 2) {
        // A pair must contain identical characters.
        if (s[i] !== s[i + 1]) {
            changes++;
        }
    }

    return changes;
};
