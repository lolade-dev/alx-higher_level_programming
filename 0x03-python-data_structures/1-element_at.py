def element_at(my_list, idx):
    for arr in range(len(my_list)):
        if (idx < 0):
            return (None)
        elif (idx > len(my_list)):
            return (None)
        elif (idx == arr):
            return (my_list[arr])
