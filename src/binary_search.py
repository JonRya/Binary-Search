# Returns the index of the value if the value exists
# Otherwise returns -1
def binary_seach(val: int, ordered_list: list[int]) -> int:
    index: int = 0

    while len(ordered_list) > 1:
        mid: int = len(ordered_list) // 2
        if val < ordered_list[mid]:
            ordered_list = ordered_list[:mid]
        elif val > ordered_list[mid]:
            index += mid
            ordered_list = ordered_list[mid:]
        else:
            index += mid
            break
    else:
        if ordered_list[0] != val:
            return -1
    
    return index


# For testing purposes
if __name__ == '__main__':
    test = [x for x in range(50)]
    val = 50
    index = binary_seach(val, test)
    print(f'Index: {index}')
    if index != -1:
        assert test[index] == val