#include <cstdio>

using namespace std;
typedef int Rank;

void merge(int arr[], Rank lo, Rank mi, Rank hi){
    int* A = arr + lo;  //A[0, hi-lo) = arr[lo,hi)
    int lb = mi - lo; int* B = new int[lb]; //B[0,lb) = arr[lo, mi)
    for(Rank i = 0; i < lb; ++i) B[i] = A[i];
    int lc = hi - mi; int* C = arr + mi; // C[0, lc) = arr[mi, hi)

    for(Rank i = 0, j = 0, k = 0; j < lb;)
        A[i++] = (lc <= k || B[j] <= C[k]) ? B[j++] : C[k++];
    
    delete [] B; // free temp array B;
}

void mergeSort(int arr[], Rank lo, Rank hi){
    if(hi - lo < 2) return;

    Rank  mi = (lo + hi) >> 1;
    mergeSort(arr, lo, mi); // 对数组前半段进行排序
    mergeSort(arr, mi, hi); // 对数组后半段进行排序
    merge(arr, lo, mi, hi); // 归并
}

void printArray(int arr[], int size){
    int i = 0;
    for(; i < size - 1; ++i)
        printf("%d, ", arr[i]);
    printf("%d", arr[i]);
    printf("\n");
}

int main(){
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr) / sizeof(arr[0]); 

    printf("Given array is \n"); 
    printArray(arr, arr_size); 

    mergeSort(arr, 0, arr_size); 

    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}