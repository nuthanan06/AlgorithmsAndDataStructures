def BubbleSort (list, counter = 0): 
    counter += 1
    size = len(list)

    for i in range(size- counter): 
        swapped = False
        if list[i] > list[i + 1]: 
            placeholder = list[i]
            list[i] = list[i+1]
            list[i+1] = placeholder
            swapped = True
    
    if counter != size and swapped: 
        return BubbleSort (list, counter)
    else:
        return list

elements = [5,9,2,1,67,34,88,34]
elements = BubbleSort(elements)
print(elements)


