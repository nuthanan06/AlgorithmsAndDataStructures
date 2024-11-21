def partition(elements, start, end): 
    pivot_index = start 
    pivot = elements[pivot_index]


    while start < end: 
        while start < len(elements) and elements[start] <= pivot: 
            start += 1
        
        while elements[end] > pivot: 
            end -= 1

        if start < end: 
            elements[start], elements[end] = elements[end], elements[start]

    elements[end], elements[pivot_index] = elements[pivot_index], elements[end]

    return end


def quick_sort(list, start, end): 
    if start < end: 
        p1 = partition(list, start, end)
        quick_sort(elements, start, p1 - 1)
        quick_sort(elements, p1 + 1, end)

elements = [11, 9, 29, 7, 2, 15, 28]
quick_sort(elements, 0, len(elements) - 1)
print(elements)