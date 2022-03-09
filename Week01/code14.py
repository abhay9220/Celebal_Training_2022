# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.


# For example:

# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i
# This prints:

# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])


# In this challenge, you will be given 2 integers, m and n. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.


# Constraints
# 1<=n<=10000
# 1<=m<=100
# 1<=length of each word in the input<=100


# Input Format

# The first line contains integers, m and n separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.


# Output Format

# Output m lines.
# The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import sys

d = defaultdict(list)
lst = list(map(int, input().split()))
n = lst[0]
m = lst[1]
for i in range(n):
    d[sys.stdin.readline().strip()].append(i+1)

for i in range(m):
    l = d[sys.stdin.readline().strip()]
    if l: print(*l)
    else: print(-1)
