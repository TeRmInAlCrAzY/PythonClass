def quicksort(arr):
    """
    Sorts a given list of elements using the Quicksort algorithm.

    The function recursively partitions the list into elements less than,
    equal to, and greater than a chosen pivot element. It then combines these
    partitions in sorted order to produce the final sorted result.

    :param arr: A list of elements to be sorted.
    :type arr: list
    :return: A new list containing the elements from the input list sorted in
        ascending order.
    :rtype: list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)