def quick_sort(array: list[int], low: int, high: int):
    if low < high:
        # * Find pivot element such that
        # * element smaller than pivot are on the left
        # * element greater than pivot are on the right
        pivot = partition(array, low, high)

        quick_sort(array, low, pivot-1)
        quick_sort(array, pivot+1, high)


def partition(array: list[int], low: int, high: int) -> int:
    # * choose the rightmost element as pivot
    pivot = array[high]

    # * pointer for greater element
    pointer = low - 1

    # * traverse through all elements
    # * compare each element with pivot
    for i in range(low, high):
        if array[i] <= pivot:
            # * If element smaller than pivot is found
            # * swap it with the greater element pointed by i
            pointer = pointer + 1

            # * Swapping element at i with element at j
            (array[i], array[pointer]) = (array[pointer], array[i])

    (array[pointer + 1], array[high]) = (array[high], array[pointer + 1])

    return pointer + 1
