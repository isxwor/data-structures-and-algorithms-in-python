''' R-1.8
Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
'''

# let's consider a list
s = [4, 8, 5, 9, 2]

# let k be any negative index
k = -2 

# equivalent positive index j
j = len(s) + k


check = s[k] == s[j]
print(check)
