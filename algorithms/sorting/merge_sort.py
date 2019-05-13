'''
    Sort a given array using divide-and-oonquer style - merge sort
'''
def _merge(left, right):

    mergedArray = []

    while (left and right):
        leftElement = left[0]
        rightElement = right[0]
        if leftElement < rightElement:
            mergedArray.append(leftElement)
            left = left[1:]
        else:
            mergedArray.append(rightElement)
            right = right[1:]

    while (left):
        mergedArray.append(left[0])
        left = left[1:]

    while (right):
        mergedArray.append((right[0]))
        right = right[1:]

    return mergedArray

def mergeSort(givenArray):

    size = len(givenArray)
    if size <= 1:
        return givenArray

    mid = size // 2
    left = mergeSort(givenArray[:mid])
    right = mergeSort(givenArray[mid:])

    return _merge(left, right)

if __name__ == '__main__':
    ta1 = []
    ta2 = [1]
    ta3 = [3,2,1]

    assert mergeSort(ta1) == [], 'Expected []'
    assert mergeSort(ta2) == [1], 'Expected [1]'
    assert mergeSort(ta3) == [1,2,3], 'Expected [1,2,3]'
