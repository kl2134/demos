'''
    Given a string, count occurrence of each char
    e.g. 'aaabb' -> a = 3, b = 2
'''

# Use dictionary to keep track of counts

def count_occurence(givenString):

    size = len(givenString)
    if size < 0:
        return

    tracker = {}
    for e in givenString:
        if not e in tracker:
            tracker[e] = 1
        else:
            tracker[e] = tracker.get(e) + 1

    return tracker


# Given an array of chars, sort the chars in ascending order by their number of occurence
# e.g. ['a', 'b', 'c', 'a', 'a', 'c'] -> ['b', 'c', 'c', 'a', 'a', 'a']

def sort_chars_by_occurence(givenArray):

    givenString = ''.join(givenArray)
    tracker = count_occurence(givenString)

    # From the tracker, assign each element of the array to an index, which corresponds to their number of occurence
    # e.g. {'a':3, 'b':1, 'c':2} -> [0, ['b'], ['c'], ['a']]
    if tracker:
        placeHolder = [0] * len(givenArray)
        for key, value in tracker.items():
            if placeHolder[value] != 0:
                temp = placeHolder[value]
                temp.append(key)
            else:
                placeHolder[value] = [key]

    # Flatten the placeHolder array and copy each element n times to the result array, according to index number
    # [0, ['b'], ['c'], ['a']] -> ['b', 'c', 'c', 'a', 'a', 'a']
    result = []
    for i in range(1, len(placeHolder)):
        if placeHolder[i] != 0:
            for element in placeHolder[i]:
                for j in range(i):
                    result.append(element)

    return result

if __name__ == '__main__':
    ta1 = ['a', 'b', 'c', 'a', 'a', 'c']
    ta2 = ['a', 'b', 'b', 'a', 'a', 'c']
    ta3 = ['a', '', 'b', 'a', 'a', 'c', 'c', 'c', '', 'b']
    assert sort_chars_by_occurence(ta1) == ['b', 'c', 'c', 'a', 'a', 'a']
    assert sort_chars_by_occurence(ta2) == ['c', 'b', 'b', 'a', 'a', 'a']
    assert sort_chars_by_occurence(ta3) == ['b', 'b', 'a', 'a', 'a', 'c', 'c', 'c']

