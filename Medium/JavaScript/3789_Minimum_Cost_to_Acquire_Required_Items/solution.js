
/**
 * LeetCode 3789 - Minimum Cost to Acquire Required Items
 *
 * @param {number} cost1
 * @param {number} cost2
 * @param {number} costBoth
 * @param {number} need1
 * @param {number} need2
 * @return {number}
 */
var minimumCost = function(cost1, cost2, costBoth, need1, need2) {
    // Number of units required by both requirements.
    const common = Math.min(need1, need2);

    // Choose between one shared item and two individual items.
    const sharedCost = Math.min(costBoth, cost1 + cost2);

    let totalCost = common * sharedCost;

    // Handle any remaining type 1 requirement.
    if (need1 > common) {
        totalCost += (need1 - common) * Math.min(cost1, costBoth);
    }

    // Handle any remaining type 2 requirement.
    if (need2 > common) {
        totalCost += (need2 - common) * Math.min(cost2, costBoth);
    }

    return totalCost;
};
