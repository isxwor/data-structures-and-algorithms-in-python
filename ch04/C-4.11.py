''' C-4.11
Describe an efﬁcient recursive function for solving the element uniqueness
problem, which runs in time that is at most O(n^2) in the worst case without
using sorting.
'''


def unique(S, index=0):
    if index == len(S)-1:
        return True
    else:
        for k in range(index+1, len(S)):
            if S[index] == S[k]:
                return False
        return unique(S, index+1)


if __name__ == '__main__':
    sequences = [
    [1, 2, 3, 4, 5, 6],
    [2, 5, 3, 8, 3, 9]
    ]
    for S in sequences:
        print(unique(S))
