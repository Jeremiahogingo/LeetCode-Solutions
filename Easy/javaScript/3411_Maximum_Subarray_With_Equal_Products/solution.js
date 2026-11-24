
/**
 * LeetCode 3411 - Maximum Subarray With Equal Products
 *
 * @param {number[]} nums
 * @return {number}
 */

// Calculate the greatest common divisor.
const gcd = (a, b) => {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }

    return a;
};

// Calculate the least common multiple.
const lcm = (a, b) => {
    return (a / gcd(a, b)) * b;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    const n = nums.length;
    let answer = 0;

    // Establish an upper bound for GCD * LCM.
    let maxLcm = 1;
    let maxValue = 1;

    for (const num of nums) {
        maxLcm = lcm(maxLcm, num);
        maxValue = Math.max(maxValue, num);
    }

    const maxProduct = maxLcm * maxValue;

    // Enumerate every possible starting position.
    for (let left = 0; left < n; left++) {
        let product = 1;
        let currentGcd = 0;
        let currentLcm = 1;

        // Extend the subarray one element at a time.
        for (let right = left; right < n; right++) {
            const num = nums[right];

            product *= num;
            currentGcd = gcd(currentGcd, num);
            currentLcm = lcm(currentLcm, num);

            // Check whether the subarray is product equivalent.
            if (product === currentGcd * currentLcm) {
                answer = Math.max(answer, right - left + 1);
            }

            // The product cannot decrease as the subarray grows.
            if (product > maxProduct) {
                break;
            }
        }
    }

    return answer;
};
