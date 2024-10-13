# Returns the index of the value if the value exists
# Otherwise returns -1
def binary_seach(val: int, ordered_list: list[int]) -> int:
    mid = len(ordered_list) // 2

    if val < ordered_list[mid]:
        mid = binary_seach(val, ordered_list[:mid])
    elif val > ordered_list[mid]:
        mid = mid + binary_seach(val, ordered_list[mid:])
    
    return mid


# For testing purposes
if __name__ == '__main__':
    test = [x for x in range(50)]
    val = 34
    index = binary_seach(val, test)
    print(f'Index: {index}')
    assert test[index] == val