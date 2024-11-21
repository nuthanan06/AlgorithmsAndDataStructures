def shell_sort(arr): 
    gap = len(arr)//2
    size = len(arr)

    while gap > 0: 
        for i in range(gap, size): 
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor: 
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap
        gap -= 1

    return arr
        
arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
print(shell_sort(arr))