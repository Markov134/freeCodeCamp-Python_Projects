def selection_sort(arr):
    for j in range(len(arr)):
        for i in range(j):
            if arr[j] < arr[i]:
                result = arr[i]
                arr[i] = arr[j]
                arr[j] = result 
    return arr

hi = [5, 16, 99, 12, 567, 23, 15, 72, 3]
result = selection_sort(hi)
print(result)

