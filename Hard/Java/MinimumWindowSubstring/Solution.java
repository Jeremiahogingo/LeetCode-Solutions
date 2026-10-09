
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }

        int[] count = new int[128];

        // Count the characters required from t
        for (char c : t.toCharArray()) {
            count[c]++;
        }

        int left = 0;
        int start = 0;
        int minLength = Integer.MAX_VALUE;
        int missing = t.length();

        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);

            // Include the current character
            if (count[current] > 0) {
                missing--;
            }
            count[current]--;

            // Shrink while the window contains all required characters
            while (missing == 0) {
                int windowLength = right - left + 1;

                if (windowLength < minLength) {
                    minLength = windowLength;
                    start = left;
                }

                char leftChar = s.charAt(left);
                count[leftChar]++;

                // Removing this character makes the window invalid
                if (count[leftChar] > 0) {
                    missing++;
                }

                left++;
            }
        }

        return minLength == Integer.MAX_VALUE
                ? ""
                : s.substring(start, start + minLength);
    }
}