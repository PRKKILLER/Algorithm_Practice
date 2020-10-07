#include <iostream>
#include <cstdio>
#include "List.h"

int main() {
    std::cout << "Hello, World!" << std::endl;
    int a[5] = {3,2,4,1,5};

    List<int> list(a, 5);  // List 模板类实例化

    list.insertionSort(list.first(), 5);

//    printf("%d \n", list.remove(list.first()));

    NodePos(int) p = list.first();
    for (int i = 0; i < list.size(); ++i) {
        printf("%d, ", p->data);
        p = p->succ;
    }

    return 0;
}
