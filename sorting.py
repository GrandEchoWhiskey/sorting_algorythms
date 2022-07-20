"""
Sorting Algorythms
by Eric Wolf
"""


def quicksort(_list:list):
    """ Quick Sort """

    if len(_list) <= 1:
        return _list
    
    pivot = _list[0]

    lower = []
    bigger = []
    same = []

    while _list:
        
        item = _list.pop()

        if item < pivot:
            lower.append(item)
            continue

        if item > pivot:
            bigger.append(item)
            continue

        same.append(item)
    
    _list.extend(quicksort(lower))
    _list.extend(same)
    _list.extend(quicksort(bigger))

    return _list


def mergesort(_list:list):
    """ Merge Sort """

    if len(_list) <= 1:
        return _list

    length = len(_list)
    left = mergesort(_list[:length//2])
    right = mergesort(_list[length//2:])

    _list.clear()

    while left or right:

        if not (left and right):

            if left:
                _list.append(left[0])
                left = left[1:]
                continue

            _list.append(right[0])
            right = right[1:]
            continue

        if left[0] < right[0]:
            _list.append(left[0])
            left = left[1:]
            continue

        _list.append(right[0])
        right = right[1:]

    return _list


def bubblesort(_list:list):
    """ Bubble Sort """
    
    for i in range(len(_list), 1, -1):

        for j in range(0, i-1):
            
            if _list[j] > _list[j+1]:
                temp = _list[j+1]
                _list[j+1] = _list[j]
                _list[j] = temp

    return _list

def selectionsort(_list:list):
    """ Selection Sort """

    for i in range(len(_list)-1):

        lowest = i

        for j in range(i, len(_list)-1):

            if _list[j] < _list[lowest]:
                lowest = j

        temp = _list[i]
        _list[i] = _list[lowest]
        _list[lowest] = temp

    return _list


