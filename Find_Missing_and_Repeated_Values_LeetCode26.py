def findMissingAndRepeatedValues(grid):
    aux_list = []
    array_result = []
    for array in grid:
        for i in array:
            aux_list.append(i)
    for i in aux_list:
        if aux_list.count(i) != 1:
            array_result.append(i)
            break
    for i in range(1,len(aux_list)+1):
        if i not in aux_list:
            array_result.append(i)
            break
    return array_result
print(findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])) 