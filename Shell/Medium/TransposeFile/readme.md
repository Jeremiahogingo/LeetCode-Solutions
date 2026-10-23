# 194. Transpose File

![LeetCode](https://img.shields.io/badge/LeetCode-194-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Language](https://img.shields.io/badge/Language-Bash-black?logo=gnubash)
![Topic](https://img.shields.io/badge/Topic-Text%20Processing-blue)

## Problem Overview

Given a text file named `file.txt` containing a rectangular matrix of words, transpose the matrix so that each original column becomes a row in the output.

For example, the first column of the input becomes the first output line, the second column becomes the second output line, and so on.

**LeetCode:** [Transpose File](https://leetcode.com/problems/transpose-file/description/)

## Approach: Bash + AWK

`awk` processes a file line by line and provides built-in variables for accessing fields and tracking records.

The solution stores the values from each column in an array, then prints each accumulated column as a separate line.

### Algorithm

1. Read each line of `file.txt`.
2. Use `NF` to determine the number of fields in the current line.
3. Iterate through each field using `$i`.
4. Store the first row's fields in an array.
5. Append subsequent rows' fields to the corresponding array entries, separated by spaces.
6. In the `END` block, print each stored column on its own line.

## Bash Implementation

```bash id="j3a7md"
awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            columns[i] = $i
        } else {
            columns[i] = columns[i] " " $i
        }
    }
}
END {
    for (i = 1; i <= NF; i++) {
        print columns[i]
    }
}' file.txt
```

## AWK Concepts

| Variable | Meaning |
|---|---|
| `NR` | Number of the current input record, usually the current line |
| `NF` | Number of fields in the current line |
| `$i` | Value of the field at position `i` |
| `columns[i]` | Stores the accumulated values for original column `i` |
| `END` | Executes after all input records have been processed |

## Example Walkthrough

### Input

`file.txt`

```text id="x4j2q9"
name age
alice 21
ryan 30
```

The input matrix is:

| Column 1 | Column 2 |
|---|---|
| name | age |
| alice | 21 |
| ryan | 30 |

### Transformation

- Column 1 becomes `name alice ryan`.
- Column 2 becomes `age 21 30`.

### Expected Output

```text id="u8h4vk"
name alice ryan
age 21 30
```

## Edge Cases

| Scenario | Expected Behavior |
|---|---|
| One row with multiple fields | Each field becomes a separate output line |
| Multiple rows and columns | Every original column becomes one output line |
| One column with multiple rows | All values are printed on a single output line |
| Words contain different character lengths | Values remain separated by single spaces |
| Empty input file | Produces no output |

The problem guarantees a rectangular matrix, meaning every row contains the same number of fields. The solution relies on this constraint when printing the accumulated columns.

## Complexity Analysis

Let \(r\) be the number of rows and \(c\) the number of columns.

- **Time Complexity:** \(O(r \times c)\), because each field is processed once.
- **Auxiliary Space Complexity:** \(O(r \times c)\), because the solution stores all transposed values in memory.

## Key Takeaways

- `awk` is useful for structured text processing in shell scripting.
- `NF` allows iteration over every field in a row.
- `$i` dynamically accesses a field by its position.
- Arrays can accumulate values across multiple input records.
- The `END` block is useful for producing output after all input has been processed.
- Transposing a matrix means converting rows into columns and columns into rows.

## Related Problems

- [193. Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/)
- [195. Tenth Line](https://leetcode.com/problems/tenth-line/)
- [192. Word Frequency](https://leetcode.com/problems/word-frequency/)

## References

- [LeetCode #194 — Transpose File](https://leetcode.com/problems/transpose-file/description/)
- [GNU AWK User's Guide](https://www.gnu.org/software/gawk/manual/)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*