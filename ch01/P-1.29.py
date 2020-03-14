''' P-1.29
Write a Python program that outputs all possible strings formed by using
the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.
'''

# ------ SOLUTION ONE ------
def permute(characters, permutation=[]):
    # When the characters is empty, a full permutation exists
    if len(characters) == 0:
        print(''.join(permutation))
    else:
        # For each element left in the characters
        for k in range(len((characters))):
            # Take the element out of the characters and put it at the end of the permutation
            permutation.append(characters.pop(k))
            # Permute the rest of the characters (recursively)
            permute(characters, permutation)
            # Take the element off the permutation and put it back in the characters
            characters.insert(k, permutation.pop())
			

# ------ SOLUTION TWO ------
def combinations(characters):
    if len(characters) <= 1:
        yield characters
    else:
        for c in combinations(characters[1:]):
            for i in range(len(characters)):
                yield c[:i] + characters[:1] + c[i:]


# -- USING BUILT-IN FUNCTION --
def built_in(characters):
    from itertools import permutations
    return permutations(characters)


if __name__ == '__main__':
    characters = ['c', 'a', 't', 'd', 'o', 'g']
    
    # -- solution one test --
    permute(characters)
    
    # -- solution two test --
    c = 0
    for x in combinations(characters):
        print(''.join(x))
        c += 1
    print(f'Total combinations: {c}\n')
    
    # -- built-in function test --
    c = 0
    for x in built_in(characters):
        print(''.join(x))
        c += 1
    print(f'Total combinations: {c}\n')
