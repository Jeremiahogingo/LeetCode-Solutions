🔍 Problem Summary

You're given:

An array of integers nums

An integer target

Your task is to return the indices of two numbers in nums that add up to target.

Assumptions:

Each input has exactly one solution.

You cannot use the same element twice.

✅ Solution: One-Pass Hash Map

This approach uses a hash map (dictionary) to store numbers and their indices as you iterate through the array. For each number, you check if the complement (i.e., target - current number) exists in the map. If it does, you've found the pair.
Scaler

This solution has a time complexity of O(n) and space complexity of O(n).