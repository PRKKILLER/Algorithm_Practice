//
// Created by 薛智钧 on 2020/4/5.
//
#include <iostream>
#include <vector>
using namespace std;

//注：auto 关键字可用于自动推导模板参数

void merge(vector<int>& arr, int lo, int mi, int hi){
    auto A = arr.begin() + lo; // A[0, hi - lo] = arr[lo, hi]

    int b_len = mi - lo; vector<int> B;
    B.assign(arr.begin() + lo, arr.begin() + mi); // B[0, mi - lo] = arr[lo, mi]

    int c_len = hi - mi; auto C = arr.begin() + mi; // C[0, hi - mi] = arr[mi, hi]

    for  (int i = 0, j = 0, k = 0; i < b_len;)
        A[i++] = (c_len <= k || B[j] <= C[k]) ? B[j++] : C[k++];

    B.clear(); // 释放B的内存
}

void mergeSort(vector<int>& arr, int lo, int hi){
    if (hi - lo < 2) return; // 递归基

    int mi = lo + (hi - lo) / 2;
    mergeSort(arr, lo, mi); // 对左半边数组进行排序
    mergeSort(arr, mi, hi); // 对右半侧数组进行排序
    merge(arr, lo, mi, hi); // 归并排序结果
}

void printVector(vector<int>& arr){
    for (int i : arr) cout << i << " ";
    cout << endl;
}

int main(){
    vector<int> arr = {1,3,4,5};
    printVector(arr);
    mergeSort(arr, 0, arr.size());
    printVector(arr);
}
