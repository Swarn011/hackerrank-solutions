# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python
# Status      Accepted
# Submitted   2026-09-29, 09:42 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    print(hash(tuple(integer_list)))
