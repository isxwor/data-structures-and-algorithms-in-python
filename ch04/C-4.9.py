''' C-4.9
Write a short recursive Python function that ﬁnds the minimum
and maximum values in a sequence without using any loops.
'''


def minmax(S, i=0):
    if i == len(S)-1:
        return S[i], S[i]
    else:
        _min, _max = minmax(S, i+1)
        return min(S[i], _min), max(S[i], _max)

S = [2, 4, 8, 7, 1, 5]
result = minmax(S)
print(result)
