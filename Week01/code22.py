# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

#          Www.HackerRankSolution.in → wWW.hACKERrANKsOLUTION.IN
#          Pythonist 2 → pYTHONIST 2


# Input Format:
#          A single line containing a string S.


# Constraints:
#          0<len(S)<=1000


# Output Format:
#         Print the modified string S.


def swap_case(s):
    q = '';
    for char in s:
        if(char.isupper()==True):
            q += (char.lower());
        elif(char.islower()==True):
            q += (char.upper());
        else:
            q += char;
    return q;

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result