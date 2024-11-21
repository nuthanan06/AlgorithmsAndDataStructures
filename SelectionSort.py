def findMinimumElement(arr): 
    minimum = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < minimum: 
            minimum = arr[i] 
            index = i

    return [minimum, index]

def SelectionSort (arr):

    for i in range(len(arr)): 
        min_index = i 
        value = findMinimumElement(arr[i:len(arr)])
        arr[i], arr[value[1] + min_index] = value[0], arr[i]
    
    return arr

arr = [4, 38, 29, 17, 21, 25,11, 32, 9]
arr = SelectionSort(arr)

print(arr)




