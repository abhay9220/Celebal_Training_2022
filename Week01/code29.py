# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#      1. Mat size must be MXN. (N is an odd natural number, and M is 3 times N.)
#      2. The design should have 'WELCOME' written in the center. 
#      3. The design pattern should only use |, . and - characters.


# Sample Designs:

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------


# Input Format:

# A single line containing the space separated values of M and N.


# Constraints:
# 3<N<101
# 15<M<303


# Output Format:

# Output the design pattern.



# Enter your code here. Read input from STDIN. Print output to STDOUT
p,q = map(int,raw_input().split())
for i in xrange(1, p, 2): 
    print ( str('.|.')*i ).center(q, '-')
print str('WELCOME').center(q, '-')
for i in xrange(p-2, -1, -2): 
    print ( str('.|.')*i ).center(q, '-')
            