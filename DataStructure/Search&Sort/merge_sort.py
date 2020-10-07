def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mi = len(arr) // 2
    left_arr = merge_sort(arr[:mi])
    right_arr = merge_sort(arr[mi:])
    return merge(left_arr, right_arr)
    
def merge(left_arr, right_arr):
    left_cur = right_cur = 0
    ret = []
    while left_cur < len(left_arr) and right_cur < len(right_arr):
        if left_arr[left_cur] < right_arr[right_cur]:
            ret.append(left_arr[left_cur])
            left_cur += 1
        else:
            ret.append(right_arr[right_cur])
            right_cur += 1
    
    ret.extend(left_arr[left_cur:])
    ret.extend(right_arr[right_cur:])
    return ret