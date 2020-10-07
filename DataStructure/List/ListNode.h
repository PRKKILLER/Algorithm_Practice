//
// Created by 薛智钧 on 2020/3/12.
//

#ifndef DATASTRUCTURE_LISTNODE_H
#define DATASTRUCTURE_LISTNODE_H

#include <cstddef>

#define NodePos(T) ListNode<T>*
typedef int Rank;

template <typename T> struct ListNode{
    // 数据；前向指针；后项指针
    T data;
    NodePos(T) pred; NodePos(T) succ;
    // 初始化
    ListNode() {}  // 针对列表中 header, trailer 的构造
    ListNode(T e, NodePos(T) p = NULL, NodePos(T) s = NULL)
        :data(e), pred(p), succ(s) {} // 默认构造器
    // 成员函数
    NodePos(T) insertAsPred(T const & e);
    NodePos(T) insertAsSucc(T const & e);
};

#include "ListNode_implementation.h"
#endif //DATASTRUCTURE_LISTNODE_H
