def bubble_sort(arr):
    n = len(arr)

    # Repeat the process for each element in the list
    for i in range(n):
        # Go through the list up to the last unsorted element
        for j in range(0, n - 1 - i):
            # If the current item is bigger than the next one, swap them
            if arr[j] > arr[j + 1]:
                # Swap using a temp variable
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

