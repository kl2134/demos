'''
    Bubble sort - O(n^2) time complexity
'''

def bubble_sort(givenArray):

    size = len(givenArray)
    if size <= 1:
        return givenArray

    for i in range(size-1):
        for j in range(i+1, size):
            if givenArray[i] > givenArray[j]:
                givenArray[i], givenArray[j] = givenArray[j], givenArray[i]

    return givenArray

if __name__ == '__main__':
    ta1 = []
    ta2 = [1]
    ta3 = [3, 2, 1]
    ta4 = [3, 2, 1, 4, 4, 6, 9, 10]
    ta5 = [3, 2, 1, 4, 4, 6, 9, 10, 0, -1, -921]

    assert bubble_sort(ta1) == [], 'Expected []'
    assert bubble_sort(ta2) == [1], 'Expected [1]'
    assert bubble_sort(ta3) == [1, 2, 3], 'Expected [1,2,3]'
    assert bubble_sort(ta4) == [1, 2, 3, 4, 4, 6, 9, 10], 'Expected [1, 2, 3, 4, 4, 6, 9, 10]'
    assert bubble_sort(ta5) == [-921, -1, 0, 1, 2, 3, 4, 4, 6, 9, 10], 'Expected [-921, -1, 0, 1, 2, 3, 4, 4, 6, 9, 10]'