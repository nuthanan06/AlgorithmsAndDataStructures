def BinarySearch(list, number, left_index, right_index):
    mid_index = (left_index + right_index)// 2
    mid_number = list[mid_index]
    if number not in list: 
        return -1
    elif mid_number < number: 
        return BinarySearch (list, number, mid_index, right_index)
    elif mid_number < number:
        return BinarySearch (list, number, left_index, mid_index)
    else: 
        return mid_index


    
list = [4,9,11,12,15, 18, 19, 21,34,57,68,91]
number = 56

print(BinarySearch(list, number, 0, len(list)))


