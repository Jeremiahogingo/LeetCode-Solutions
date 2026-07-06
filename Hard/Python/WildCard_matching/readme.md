🔍 Problem Description

    You are given:

    A string s

    A pattern p

    Your task: return true if the entire string s matches the pattern p, else return false.

    The pattern may contain two special wildcard characters:

    ? — Matches exactly one character (any single character). 
    Design Gurus
    +1

    * — Matches any sequence of characters (including the empty sequence) 
    AlgoMonster
    +1

    Important: the match must cover the whole string s (not just a substring). 
    SparkCodehub

    📌 Example Cases

    s = "aa", p = "a" → false (pattern too short) 
    SparkCodehub
    +1

    s = "aa", p = "*" → true (* can match "aa") 
    GeeksforGeeks

    s = "cb", p = "?a" → false (? matches c, but a doesn’t match b) 
    Design Gurus

    s = "adceb", p = "*a*b" → true (for example * → "adce", then a, then * → "", then b) 
    AlgoMonster
    +1

🛠 Why It’s Challenging

    The * wildcard means you may need to match zero, one, or many characters — this often leads to many possible ways of matching, making naive recursion exponential. 
    AlgoMonster
    +1

    You need to consider the entire string and entire pattern, including leftover characters in either.

    Edge cases like an empty string, pattern consisting only of *, or many consecutive *s need careful handling.

🚀 Common Solution Approaches
    1. Recursion + Memoization (Top-Down)

        Define match(i, j) meaning: does s[i:] match p[j:]?

        Base cases:

        If j == len(p), match only if i == len(s).

        If i == len(s), then the remainder p[j:] must all be *s to match. 
        Design Gurus

        Recurrence:

        If p[j] is a regular character or ?: check if i < len(s) and (p[j] == s[i] or p[j] == '?'), then recurse match(i+1, j+1).

        If p[j] is *: two possibilities:

        * matches zero chars → match(i, j+1)

        * matches one or more chars → match(i+1, j)

        Memoize (i, j) so you don’t recompute. Time ≈ O(m * n) where m = len(s), n = len(p). 
        AlgoMonster
        +1

    2. Dynamic Programming (Bottom-Up)

        Create a 2D boolean table dp[i][j] meaning: whether s[:i] (first i chars) matches p[:j]. 
        Design Gurus
        +1

        Dimensions: (m+1) × (n+1) (include empty prefixes)

        Initialization:

        dp[0][0] = true: empty string matches empty pattern.

        For j>0, dp[0][j] = dp[0][j-1] and p[j-1] == '*' (because only * can match empty string) 
        SparkCodehub

        Filling rule: for i=1..m, j=1..n:

        If p[j-1] is a letter or ?:
        dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '?')

        Else if p[j-1] == '*':
        dp[i][j] = dp[i][j-1] (treat * as empty) or dp[i-1][j] (treat * as matching one more char) 
        AlgoMonster
        +1

        The answer is dp[m][n].

        Time complexity: O(m * n), space: O(m * n) (can be optimized to O(n)).

        ✅ What to Watch Out For

            Case when s is empty but p has only *s → should return true.

            Case when p is empty but s is non-empty → false.

            Many consecutive *s behave the same as one * (you can simplify pattern by collapsing *** → * but not strictly required). 
            Design Gurus

            Off-by-one errors when indexing DP table.

            Pattern matching must be complete, not partial.