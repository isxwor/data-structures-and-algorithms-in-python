''' R-4.1
Describe a recursive algorithm for ﬁnding the maximum element in a
sequence, S, of n elements. What is your running time and space usage?
'''


S = [4, 5, 2, 8, 1]


def find_max(S, n=len(S)-1):
    if n == 0:
        return S[n]
    else:
        return max(S[n], find_max(S, n-1))

print(find_max(S))

# Running time is O(n)
# Space is also O(n), since recursion depth is 1 + n.

# However, we can improve space usage by using binary recursion.


def binary_max(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return max(binary_max(S, start, mid), binary_max(S, mid, stop))

print(binary_max(S, 0, len(S)))

# Running time is still O(n)
# But Space is O(log n). Since, the size of the range is divided in half at
# each recursive call, and so the recursion depth is 1 + log₂n and hence,
# O(log n) space usage.
