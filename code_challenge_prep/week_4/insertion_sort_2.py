def insertion_sort(list):
    # Return a sorted list.
    for i in range(1,len(list)):
        temp = list[i]
        j=1
        while temp < list[i-j] and i-j>=0:
            list[i-j+1] = list[i-j]
            j=j+1
        list[i-j+1] = temp

    return list


my_array = [54,26,93,17,77,31,44,55,20,1, 100]
print (insertion_sort(my_array))
