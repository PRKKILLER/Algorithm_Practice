# 堆排序实现 (大顶堆)

def heap_sort(arr):
    sz = len(arr)

    # 构建大顶堆
    for i in range(sz // 2 - 1, -1, -1): # 从第一个非叶子节点开始，从上到下调整
        adjust_heap(arr, i , sz) # 自上而下调整

    # 迭代调整堆顺序
    for j in range(sz - 1, 0, -1):
        swap(arr, 0, j) # 将堆顶移到数组末尾，即将最大值移到数组末尾
        adjust_heap(arr, 0, j) # 对堆顶元素进行调整，恢复二叉堆


def adjust_heap(arr, i, sz):
    tmp = arr[i]
    k = i * 2 + 1
    while k < sz:
        if k + 1 < sz and arr[k] < arr[k + 1]:
            k += 1
        if arr[i] < arr[k]: # 若父节点 < 子节点，则下沉父节点，上浮子节点
            arr[i] = arr[k]
            i = k
        else: 
            break

        k = k * 2 + 1

    arr[i] = tmp

def build_heap(arr):
    sz = len(arr)
    for i in range(sz // 2 - 1, -1, -1):
        adjust_heap(arr, i, sz)

def del_max(heap):
    sz = len(heap)
    swap(arr, 0, sz - 1) # 将最大节点与最后一个节点交换
    heap.pop() # 删除最大节点
    adjust_heap(arr, 0, sz - 1) # 调整堆，恢复为大顶堆


def swap(arr, i, j):
    arr[0], arr[j] = arr[j], arr[0]

if __name__ == "__main__":
    arr = [3,6,-1,4,5]
    heap_sort(arr)
    print(arr)