import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[] KEYPAD = {
        "", "", "abc", "def", "ghi",
        "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();

        if (digits == null || digits.isEmpty()) {
            return result;
        }

        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(
        String digits,
        int index,
        StringBuilder current,
        List<String> result
    ) {
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        String letters = KEYPAD[digits.charAt(index) - '0'];

        for (int i = 0; i < letters.length(); i++) {
            current.append(letters.charAt(i));

            backtrack(digits, index + 1, current, result);

            current.deleteCharAt(current.length() - 1);
        }
    }
}