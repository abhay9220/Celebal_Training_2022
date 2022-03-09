# collections.OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Example

# Code

# >>> from collections import OrderedDict
# >>> 
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>> 
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>> 
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>> 
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


# Task

# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.


# Input Format

# The first line contains the number of items, N.
# The next N lines contains the item's name and price, separated by a space.


# Constraints
# 0<N<=100


# Output Format

# Print the item_name and net_price in order of its first occurrence.




# Solution :

#                         from collections import OrderedDict
# n, d = int(input()), OrderedDict()
# for _ in range(n):
#     line = input().rstrip().split()
#     item_name, net_price = ' '.join(line[:-1]), int(line[-1])
#     if item_name in d: d[item_name] += net_price
#     else: d[item_name] = net_price

# for item in sorted(sorted(d, key=lambda t: t[0])):
#     print(item, d[item])
                    

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*;
N = int(input());
d = OrderedDict();
for i in range(N):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(d.get(itemName)):
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
for i in d.keys():
    print(i, d[i])


