//
// Created by 薛智钧 on 2020/4/5.
//
#include <cstdio>

static void adjustHeap(int arr[], int i, int len){
    int tmp = arr[i]; // 缓存当前元素
    for (int k = i * 2 + 1; k < len; k = k * 2 + 1){ // 从元素i的左孩子开始
        if (k + 1 < len && arr[k] < arr[k + 1]) ++k; //若左孩子节点小于右孩子，则将k指向右孩子

        if (tmp < arr[k]){ // 若子节点值大于父节点，将子节点值赋值给父节点，不用交换
            arr[i] = arr[k];
            i = k;
        }else{
            break;
        }
    }
    arr[i] = tmp;   // tmp放到最终位置
}

static void swap(int arr[], int a, int b){
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
}

void heapSort(int arr[], int len){
    // 1. 构建大顶堆
    for (int i = len / 2 - 1; i >= 0; --i){
        // 从第一个非叶子节点开始，从上到下调整
        adjustHeap(arr, i, len);
    }

    // 迭代调整堆结构
    for (int j = len - 1; j > 0; --j){
        swap(arr, 0, j); // 堆顶和堆尾元素互换
        adjustHeap(arr, 0, j); // 对当前堆顶元素调整
    }
}

static void printArray(int arr[], int len){
    int i = 0;
    for(; i < len - 1; ++i)
        printf("%d, ", arr[i]);
    printf("%d", arr[i]);
    printf("\n");
}

int main(){
    int arr[] = {3,9,7,5,6,8,8};
    int len = sizeof(arr) / sizeof(arr[0]);

    printf("The given array is: \n");
    printArray(arr, len);
    heapSort(arr, len);
    printf("The sorted result is: \n");
    printArray(arr, len);
    return 0;
}


