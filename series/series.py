

def slices(num_string, slice_length):
    slice_list = []
    total_slices = len(num_string) - slice_length + 1

    if total_slices <= 0 or slice_length <= 0:
        raise ValueError
    
    for i in range(total_slices):
        part = list(num_string[i:slice_length+i])
        part = [int(j) for j in part]
        slice_list.append(part)
        
    return slice_list
