def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i  # Start by assuming the current index has the smallest value

        # Find the index of the smallest value in the remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the values using a temporary variable (temp)
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    return arr
