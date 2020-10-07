//
// Created by 薛智钧 on 2020/4/6.
//
#include <iostream>
#include <vector>
using namespace std;

static void swap(vector<int>& arr, int a, int b){
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
}

static void adjustHeap(vector<int>& arr, int i, int len){
    int tmp = arr[i];
    for (int k = 2 * i + 1; k < len; k = k * 2 + 1){
        if (k + 1 < len && arr[k] < arr[k + 1]) ++k;
        if (tmp < arr[k]){
            arr[i] = arr[k];
            i = k;
        }
    }
    arr[i] = tmp;
}

void heapSort(vector<int>& arr, int len){
    // 建大顶堆
    for (int i  = len / 2 - 1; i >=0; --i){
        adjustHeap(arr, i, len);
    }

    // 迭代调整堆结构
    for (int j = len - 1; j > 0; --j){
        swap(arr, 0, j);
        adjustHeap(arr, 0 ,j);
    }
}

static void printArray(vector<int>& arr){
    for (int i : arr)
        cout << i << " ";
    cout << endl;
}

int main(){
    vector<int> arr = {3,2,5,5,6,7,1};
    cout << "The given array is: " << endl;
    printArray(arr);

    heapSort(arr, arr.size());
    cout << "The sorted array is: " << endl;
    printArray(arr);
}
