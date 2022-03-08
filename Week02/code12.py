# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

# To read more about the functions in this module, check out their documentation here.

# You are given a list of N lowercase English letters. For a given integer k, you can select any k indices (assume 1-based indexing) with a uniform probability from the list.

# Find the probability that at least one of the k indices selected will contain the letter: 'a'.


# Input Format

# The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

# The third and the last line of input contains the integer K, denoting the number of indices to be selected.


# Output Format

# Output a single line consisting of the probability that at least one of the k indices selected contains the letter:'a'.

# Note: The answer must be correct up to 3 decimal places.


# Constraints
# 1<=N<=10
# 1<=K<=N


# All the letters in the list are lowercase English letters.



# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
D = input().split()
K = int(input())


from itertools import combinations

contain = 0
total = 0

for c in combinations(D, K):
    if "a" in c:
        contain += 1
    total += 1
print(contain/total)