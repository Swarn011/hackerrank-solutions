# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-09-29, 09:42 p.m.
# Technique   tuple-hashing-conversion
# Time        O(n)
# Space       O(n)
# Insight     The implementation converts a list of integers into an immutable tuple to enable the computation of its hash value.
# Interview   Before: "How do I compute the hash of a sequence?" After: "By converting the input list into a tuple, we can pass it to the built-in hash function, which operates in O(n) time to process all n elements."
# Pitfalls    (1) Attempting to hash a list directly will raise a TypeError because lists are mutable and unhashable.  (2) Using input() instead of raw_input() in Python 2 environments may cause unexpected behavior with input parsing.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    print(hash(tuple(integer_list)))
