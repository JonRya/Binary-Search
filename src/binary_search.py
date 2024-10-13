# Returns the index of the value if the value exists
# Otherwise returns -1
def binary_seach(val: int, ordered_list: list[int]) -> int:
    index: int = 0

    # Loop until length of ordered list is 1
    while len(ordered_list) > 1:
        # Get middle index
        mid: int = len(ordered_list) // 2

        # If val is less than the middle value search in the left half
        if val < ordered_list[mid]:
            ordered_list = ordered_list[:mid]
        # If val is more than the middle value search in the right half
        elif val > ordered_list[mid]:
            index += mid
            ordered_list = ordered_list[mid:]
        # If val is equal to the middle value
        else:
            index += mid
            break
    # Execute once the length of ordered list is 1
    else:
        # Value doesn't exist
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