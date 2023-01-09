def int_list(list_measures):
    temp = []
    [temp.append(x.strip()) for x in list_measures if x.strip() not in temp]
    return sorted(temp)
