#include <cstdio>

using namespace std;

class Fib {
    int f, g;
public:
    Fib(int n) {
        f = 1;
        g = 0;
        while (g < n)
            next();
    }
    int get() { return g; }
    int next() { g += f; f = g - f; return g; }
    int prev() { f = g - f; g -= f; return g; }
};

int fibSearch(int A[], int e, int lo, int hi) {  // 返回 fib 查找的查找长度
    Fib fib(hi - lo);
    int cmp_times = 0;
    while (lo < hi) {
        while (hi - lo < fib.get()) fib.prev();
        int mi = lo + fib.get() - 1;
        if (e < A[mi]) {
            hi = mi;
            cmp_times++;
        } else if (A[mi] < e) {
            lo = mi + 1;
            cmp_times += 2;
        } else {
            return cmp_times + 2;
        }
    }
    return cmp_times;
}

int binSearch(int A[], int e, int lo, int hi) {  // 返回二分查找（版本A）的查找长度
    int cmp_times = 0;
    while (lo < hi) {
        int mi = (lo + hi) >> 1;
        if (e < A[mi]) {
            hi = mi;
            cmp_times++;
        } else if (A[mi] < e) {
            lo = mi + 1;
            cmp_times += 2;
        } else {
            return cmp_times + 2;
        }
    }
    return cmp_times;
}

int main() {
    for (int i = 5; i < 200; i++) {
        int *A = new int[i];
        for (int j = 0; j < i; j++)
            A[j] = j * 2;
        int bin_success = 0;
        int bin_fail = 0;
        int fib_success = 0;
        int fib_fail = 0;
        for (int j = 0; j < i; j++) {
            bin_success += binSearch(A, j * 2, 0, i);
            fib_success += fibSearch(A, j * 2, 0, i);
        }
        for (int j = 0; j < i + 1; j++) {
            bin_fail += binSearch(A, j * 2 - 1, 0, i);
            fib_fail += fibSearch(A, j * 2 - 1, 0, i);
        }
        printf("n=%d, bin success %f, bin fail %f, fib success %f, fib fail %f\n",
            i,
            (double)bin_success / i, (double)bin_fail / (i + 1),
            (double)fib_success / i, (double)fib_fail / (i + 1));
        delete[] A;
    }
    return 0;
}