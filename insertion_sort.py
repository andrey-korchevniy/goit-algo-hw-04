def insertion_sort(lst):
    new_list = lst.copy()
    for i in range(1, len(new_list)):
        key = new_list[i]
        j = i-1
        while j >=0 and key < new_list[j] :
                new_list[j+1] = new_list[j]
                j -= 1
        new_list[j+1] = key 
    return new_list
