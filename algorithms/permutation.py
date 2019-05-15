'''
    General demonstration of permutation algorithm using a cache
    The purpose is to get all permutation of index numbers such that we can generate corresponding strings
    Algorithm -
        end -> []
        start -> [0,1,2]
        For each index of the start,
            generate a newEnd by appending the num of start at index i : newEnd -> [0]
            remove that num from start : newStart -> [1,2]

            Call the recursive function with newEnd and newStart, while saving each newStart in a cache,
            so it won't be recalculated in further recursive calls

            cache -> {'12' : [1,2]}

            This goes on until start is exhausted.

'''
def _permutate(end, start, cache, permutations):
    skey = ''.join([str(s) for s in start])

    # Check if the start is in cache, if so no need to recalculate, append the end and add it to permutations
    if skey in cache.keys():
        p = end + cache.get(skey)
        permutations.append(p)
    # Base case - if start is no more, append the flipped version and add it to permutations
    elif len(start) <= 1:
        p = end + start
        permutations.append(p)
    # Recursive case - nothing above is satisfied, add the start to cache, and go into recursive calls
    else:
        cache[skey] = start
        for i in range(len(start)):
            newEnd = end + [start[i]]
            newStart = [x for x in start if x != start[i]]
            _permutate(newEnd, newStart, cache, permutations)

# Wrapper function
def generatePermutations(start):
    cache = {}
    permutations = []
    _permutate([], start, cache, permutations)
    return permutations

if __name__ == '__main__':
    
    permutations = generatePermutations([0,1,2,3])

    # Demonstration of a string permutation
    s = 'abcd'
    for p in permutations:
        print(s[p[0]] + s[p[1]] + s[p[2]] + s[p[3]])