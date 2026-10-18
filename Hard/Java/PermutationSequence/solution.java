import java.util.ArrayList;
import java.util.List;

class Solution {
    public String getPermutation(int n, int k) {
        int[] factorial = new int[n + 1];
        factorial[0] = 1;

        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        List<Integer> numbers = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        // Convert k to zero-based indexing
        k--;

        StringBuilder result = new StringBuilder();

        for (int remaining = n; remaining > 0; remaining--) {
            int blockSize = factorial[remaining - 1];
            int index = k / blockSize;

            result.append(numbers.remove(index));

            k %= blockSize;
        }

        return result.toString();
    }
}
