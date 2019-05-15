'''
    Quick sort
'''

def _partition(givenArray, startIndex, endIndex):
    pivot = givenArray[startIndex]
    newPivotIndex = startIndex + 1

    # Iterate over elements excluding the pivot at startIndex
    for i in range(startIndex+1, endIndex):
        # If less than pivot, swap the nums and increment newPivotIndex by 1
        if givenArray[i] < pivot:
            givenArray[newPivotIndex], givenArray[i] = givenArray[i], givenArray[newPivotIndex]
            newPivotIndex += 1

    # All nums less than pivot are moved close to pivot at startIndex
    # Now move the pivot num to newPivotIndex-1, so all nums less than pivot are on the left side of the array
    givenArray[startIndex], givenArray[newPivotIndex-1] = givenArray[newPivotIndex-1], givenArray[startIndex]

    # Return the pivot position for further recursive calls
    return newPivotIndex-1

def _quickSort(givenArray, start, end):
    if start < end:
        pivotIndex = _partition(givenArray, start, end)
        _quickSort(givenArray, start, pivotIndex)
        _quickSort(givenArray, pivotIndex+1, end)

def quickSort(givenArray):

    size = len(givenArray)
    if size <= 1:
        return givenArray

    _quickSort(givenArray, 0, size)

    return givenArray

if __name__ == '__main__':
    ta1 = []
    ta2 = [1]
    ta3 = [3, 2, 1]
    ta4 = [3, 2, 1, 4, 4, 6, 9, 10]
    ta5 = [3, 2, 1, 4, 4, 6, 9, 10, 0, 0, 0, -1, -921]

    assert quickSort(ta1) == [], 'Expected []'
    assert quickSort(ta2) == [1], 'Expected [1]'
    assert quickSort(ta3) == [1, 2, 3], 'Expected [1,2,3]'
    assert quickSort(ta4) == [1, 2, 3, 4, 4, 6, 9, 10], 'Expected [1, 2, 3, 4, 4, 6, 9, 10]'
    assert quickSort(ta5) == [-921, -1, 0, 0, 0, 1, 2, 3, 4, 4, 6, 9, 10], 'Expected [-921, -1, 0, 1, 2, 3, 4, 4, 6, 9, 10]'