import random 

def qsort(arr):
    n = len(arr)
    _qsort(arr, 0, n-1)

def _qsort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        _qsort(arr, lo, p-1)
        _qsort(arr, p+1, hi)

def partition(arr, lo, hi):
    random.shuffle(arr[lo : hi+1])
    pivot = arr[lo]
    while lo < hi:
        while lo < hi and pivot <= arr[hi]: hi -= 1
        if lo < hi: 
            arr[lo] = arr[hi]
            lo += 1
        while lo < hi and arr[lo] <= pivot: lo += 1
        if lo < hi:
            arr[hi] = arr[lo]
            hi -= 1
    arr[lo] = pivot # important
    return lo

if __name__ == "__main__":
    a = [2,34,5,-1,9,10]
    qsort(a)
    print(a)