//
// Created by 薛智钧 on 2020/4/5.
//
#include <cstdio>
#include <cstdlib>
#include <algorithm>

int partition(int arr[], int lo, int hi){
    std::swap(arr[lo], arr[lo + rand() % (hi - lo)]); // 随机交换
    hi--;
    int pivot = arr[lo];
    while (lo < hi){
        while (lo < hi && pivot <= arr[hi]) --hi; // 向左拓展G
        if (lo < hi) arr[lo++] = arr[hi]; // 小于pivot者，归入左侧
        while (lo < hi && arr[lo] <= pivot) ++lo; // 向右拓展L
        if (lo < hi) arr[hi--] = arr[lo]; // 大于pivot者，归入右侧
    }
    arr[lo] = pivot;
    return lo;
}

void quickSort(int arr[], int lo, int hi){
    if (hi - lo < 2) return;

    int mi = partition(arr, lo, hi); // 获取轴点位置
    quickSort(arr, lo, mi); // 对轴点左侧进行排序
    quickSort(arr, mi + 1, hi);  // 对轴点右侧进行排序
}

void printArray(int arr[], int len){
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
    quickSort(arr, 0, len);
    printf("The sorted result is: \n");
    printArray(arr, len);
    return 0;
}

