# O(1),S(1)
def parent(i):
    return i / 2


# O(1),S(1)
def left(i):
    return 2 * i


# O(1),S(1)
def right(i):
    return 2*i + 1


# O(log n),S(1)
def max_heapify(elements, i):
    l = left(i)
    r = right(i)
    heap_size = elements[0]
    if l <= heap_size and elements[l] > elements[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and elements[r] > elements[largest]:
        largest = r
    if largest != i:
        elements[i], elements[largest] = elements[largest], elements[i]
        max_heapify(elements, largest)


# O(n/2) S(1)
def build_max_heap(elements):
    offset = len(elements) / 2
    while offset != 0:
        max_heapify(elements, offset)
        offset -= 1


# O(n log n),S(1)
def heap_sort(elements):
    build_max_heap(elements)
    i = elements[0]
    while i != 1:
        elements[1], elements[i] = elements[i], elements[1]
        elements[0] -= 1
        i -= 1
        max_heapify(elements, 1)


def test_parent():
    assert 1 == parent(3) and 4 == parent(8)


def test_left():
    assert 2 == left(1) and 6 == left(3)


def test_right():
    assert 7 == right(3) and 5 == right(2)


def test_max_heappify():
    test = [5, 7, 8, 9, 2, 1, 7, 8]
    test[0] = len(test) - 1
    max_heapify(test, 1)
    print test[1:]


def test_build_max_heap():
    test = [5, 7, 8, 9, 2, 1, 7, 8]
    build_max_heap(test)
    print test[1:]


def test_heap_sort():
    test = [5, 7, 8, 9, 2, 1, 7, 8]
    test[0] = len(test) - 1
    heap_sort(test)
    print test[1:]

test_parent()
test_left()
test_right()
test_max_heappify()
test_build_max_heap()
test_heap_sort()