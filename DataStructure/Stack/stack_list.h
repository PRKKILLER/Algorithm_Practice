//
// Created by 薛智钧 on 2020/3/13.
//

#ifndef DATASTRUCTUER_STACK_LIST_H
#define DATASTRUCTUER_STACK_LIST_H

#include "../List/List.h"

template <typename T> class Stack: public List<T> {
public:
    // 注意template inherent （模板继承）的情况
    // 这样的情况下，当需要使用基类的函数，需要手动明确
    void push(T const& e){ this->insertAsLast(e); }
    T pop() { return remove ( this->last() ); }
    T& top(){ return this->last()->data; }
};
#endif //DATASTRUCTUER_STACK_LIST_H
