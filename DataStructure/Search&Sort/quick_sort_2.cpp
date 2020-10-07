//
// Created by 薛智钧 on 2020/4/5.
//
#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int partition(vector<int>& arr, int lo, int hi){
    random_shuffle(arr.begin() + lo, arr.begin() + hi);
    int pivot = arr[lo]; --hi;
    while(lo < hi){
        while(lo < hi && pivot <= arr[hi]) --hi;
        if (lo < hi) arr[lo++] = arr[hi];
        while(lo < hi && arr[lo] <= pivot) ++lo;
        if (lo < hi) arr[hi--] = arr[lo];
    }
    arr[lo] = pivot;
    return lo;
}

void quickSort(vector<int>& arr, int lo, int hi){
    if (hi - lo < 2) return;

    int mi = partition(arr, lo, hi);
    quickSort(arr, lo, mi);
    quickSort(arr, mi + 1, hi);
}

void printArray(vector<int>& arr){
    for (int i : arr)
        cout << i << " ";
    cout << endl;
}

int main(){
    vector<int> arr = {3,2,5,5,6,7,1};
    cout << "The given array is: " << endl;
    printArray(arr);

    quickSort(arr, 0, arr.size());
    cout << "The sorted array is: " << endl;
    printArray(arr);
}