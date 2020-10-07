//
// Created by 薛智钧 on 2020/3/12.
//

#ifndef DATASTRUCTURE_LIST_IMPLEMENTATION_H
#define DATASTRUCTURE_LIST_IMPLEMENTATION_H


#include <cstdio>


template <typename T> void List<T>::init() { // 默认初始化函数
    header = new ListNode<T>;
    trailer = new ListNode<T>;
    header->succ = trailer; header->pred = NULL;
    trailer->pred = header; trailer->succ = NULL;
    _size = 0;
}

template <typename T> int List<T>::clear() { // 列表清空函数
    int oldSize = _size;
    while (_size > 0) remove(header->succ);
    return oldSize;
}

template <typename T> void List<T>::copyNodes(NodePos(T) p, int n) {
    init(); //创建头尾哨兵
    while (0 < n--) {insertAsLast(p->data); p = p->succ;}
}

template <typename T> List<T>::List(const List<T> &L) {copyNodes(L.first(), L.size());}

template <typename T> List<T>::List(NodePos(T) p, int n) {copyNodes(p, n);}

template <typename T> List<T>::List(const List<T> &L, Rank r, int n) {
    NodePos(T) p = L.first();
    while (r-- > 0) p = p->succ;
    copyNodes(p, n);
}
template <typename T> List<T>::List(const T arr[], int n) {
    init();
    for (int i = 0; i < n; ++i) insertAsLast(arr[i]);
}

template <typename T> List<T>::~List() {clear(); delete header; delete trailer;}

template <typename T> T & List<T>::operator[](Rank r) const {
    NodePos(T) p = first();
    while (0 < r--) p = p->succ;
    return p->data;
}

template <typename T> NodePos(T) List<T>::find(const T &e, int n, NodePos(T) p) const {
    while (0 < n--){
        if (e == ((p->pred)->data)) return p;
    }
    return NULL;
}

template <typename T> NodePos(T) List<T>::search(const T &e, int n, NodePos(T) p) const {
    do {
        p = p->pred; n--;
    } while ( ( -1 < n ) && ( e < p->data ) );
    return p;  // 返回列表节点p位置前n项中不大于e的最后一项
}

// 在p及其n-1个后继中查找最大者
template <typename T> NodePos(T) List<T>::selectMax(NodePos(T) p, int n) const {
    NodePos(T) max = p;
    for (NodePos(T) cur = p; 1 < n ; --n) {
        if((cur = cur->succ)->data >= max->data)
            max = cur;  // cur->data >= max->data
    }
    return max;
}

template <typename T> NodePos(T) List<T>::insertAsFist(const T &e) {
    _size++;
    return header->insertAsSucc(e);
}

template <typename T> NodePos(T) List<T>::insertAsLast(const T &e) {
    _size++;
    return trailer->insertAsPred(e);
}

template <typename T> NodePos(T) List<T>::insertAhead(const T &e, NodePos(T) p) {
    _size++;
    return p->insertAsPred(e);
}

template <typename T> NodePos(T) List<T>::insertBehind(const T &e, NodePos(T) p) {
    _size++;
    return p->insertAsSucc(e);
}

template <typename T> T List<T>::remove(NodePos(T) p) {
    T e = p->data;
    p->pred->succ = p->succ;
    p->succ->pred = p->pred;
    delete p; -- _size;
    return e;
}

template <typename T> int List<T>::deduplicate() {
    if (_size < 2) return 0;
    int oldSize = _size;
    NodePos(T) p = first();
    for(Rank i = 0; p != trailer; p = p->succ){
        if(NodePos(T) q = find(p->data, i, p))
            remove(q);
        else
            ++i;
    }
    return oldSize - _size;
}

template <typename T> int List<T>::uniquify() {
    if (_size < 2) return 0;
    int oldSize = _size;
    NodePos(T) p = first(); NodePos(T) cur;
    while ((cur = p->succ) != trailer){
        if (p->data != cur->data) p = cur;
        else remove(cur);
    }
    return oldSize - _size;
}

template<typename T> void List<T>::reverse() {
    NodePos(T) p= header; NodePos(T) q = trailer;
    for (int i = 0; i < _size; i += 2) {
        T temp = (p->succ)->data;
        (p->succ)->data = (q->pred)->data;
        (q->pred)->data = temp;
        p = p->succ; q = q->pred;
    }
}

// 选择排序: 对列表起始于p开始的n个节点进行排序
// 每次选取列表中最大元素，插入到tail处
template<typename T> void List<T>::selectionSort(NodePos(T) p, int n) {
    NodePos(T) head = p->pred; NodePos(T) tail = p;
    for (int i = 0; i < n; ++i) {
        tail = tail->succ;
    }
    while (1 < n){
        insertAhead(remove(selectMax(head->succ, n)), tail);
        tail = tail->pred;
        --n;
    }
}

// 插入排序: 对列表起始于p开始的n个节点进行排序
template<typename T> void List<T>::insertionSort( NodePos(T) p, int n) {
    for (Rank r = 0; r < n; ++r){
        insertBehind(p->data, search(p->data, r, p));
        p = p->succ;
        remove(p->pred);
    }
}

#endif //DATASTRUCTURE_LIST_IMPLEMENTATION_H
