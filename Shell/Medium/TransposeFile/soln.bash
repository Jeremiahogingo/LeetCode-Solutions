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