'''
    Selection sort -
        - Find the min or max element in the array and swap it with the first element at each iteration.
    O(n^2) time complexity
'''

def selectionSort(givenArray):

    size = len(givenArray)
    if size <= 1:
        return givenArray
    '''
        For each iteration, set the starting i to min
        For each i+1, update min to i+1 if the element is smaller
        At the end of that iteration, swap the elements
    '''
    for i in range(size):
        minimum = i
        for j in range(i+1, size):
            if givenArray[minimum] > givenArray[j]:
                minimum = j
        givenArray[i], givenArray[minimum] = givenArray[minimum], givenArray[i]
        
    return givenArray

if __name__ == '__main__':
    ta1 = []
    ta2 = [1]
    ta3 = [3, 2, 1]
    ta4 = [3, 2, 1, 4, 4, 6, 9, 10]
    ta5 = [3, 2, 1, 4, 4, 6, 9, 10, 0, -1, -921]

    assert selectionSort(ta1) == [], 'Expected []'
    assert selectionSort(ta2) == [1], 'Expected [1]'
    assert selectionSort(ta3) == [1, 2, 3], 'Expected [1,2,3]'
    assert selectionSort(ta4) == [1, 2, 3, 4, 4, 6, 9, 10], 'Expected [1, 2, 3, 4, 4, 6, 9, 10]'
    assert selectionSort(ta5) == [-921, -1, 0, 1, 2, 3, 4, 4, 6, 9, 10], 'Expected [-921, -1, 0, 1, 2, 3, 4, 4, 6, 9, 10]'
                
