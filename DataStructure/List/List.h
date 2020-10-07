//
// Created by 薛智钧 on 2020/3/12.
//

#ifndef DATASTRUCTURE_LIST_H
#define DATASTRUCTURE_LIST_H


#include "ListNode.h"

template <typename T> class List{

private:
    int _size; NodePos(T) header; NodePos(T) trailer;

protected:
    void init(); //列表创建时的初始化
    int clear(); // 清除所有节点
    void copyNodes(NodePos(T), int); //复制列表中z自位置p起的第n项

public:
    //构造函数
    List(){init();} // 默认构造函数
    List(List<T> const &L);  //整体复制列表
    List(List<T> const &L, Rank r, int n); //复制列表中自第r项起的第n项
    List(NodePos(T) p, int n); //复制列表中自节点p起的第n项
    List(const T arr[], int n);  // 通过向量构造列表
    //析构函数
    ~List(); //释放（包括header, trailer在内的的所有节点）
    
    /**只读访问接口**/
    Rank size() const { return _size;}
    bool empty() const { return _size <= 0;}
    bool valid(NodePos(T) p) const { // 判断位置p是否合法
        return p && (p != trailer) && (p != header);
    }
    T& operator[] (Rank r) const; // 重载，使列表支持寻秩访问数据
    NodePos(T) first() const { return header->succ;}
    NodePos(T) last() const { return trailer->pred;}
    // 无序列表区间查找
    NodePos(T) find(T const &e) const { // 在整个无序列表区间查找
        return find(e, _size, trailer);
    }
    NodePos(T) find(T const &e, int n, NodePos(T) p) const;
    // 有序列表区间查找
    NodePos(T) search(T const &e) const {
        return search(e, _size, trailer);
    }
    NodePos(T) search(T const &e, int n, NodePos(T) p) const;
    // 查找区间最大值
    NodePos(T) selectMax(NodePos(T) p, int n) const; // 在p及其n-1个后继中寻找最大者
    NodePos(T) selectMax() const { return selectMax(first(), _size);}

    /**可写访问接口**/
    // 插入节点
    NodePos(T) insertAsFist(T const &e);
    NodePos(T) insertAsLast(T const &e);
    NodePos(T) insertAhead(T const &e, NodePos(T) p);
    NodePos(T) insertBehind(T const &e, NodePos(T) p);
    //删除节点
    T remove(NodePos(T) p); //删除合法位置p处的节点，并返回节点的数据
    // 归并排序
//    void merge ( NodePos(T)&, int, List<T>&, NodePos(T), int ); //归并
//    void mergeSort ( NodePos(T)&, int ); //对从p开始连续的n个节点归并排序
//    void merge ( List<T>& L ) { merge ( first(), size(), L, L.first(), L._size ); } //全列表归并
    //选择排序
    void selectionSort ( NodePos(T) p, int n); //对从p开始连续的n个节点选择排序
    //插入排序
    void insertionSort ( NodePos(T) p, int n); //对从p开始连续的n个节点插入排序
    int deduplicate(); //无序去重
    int uniquify(); //有序去重
    void reverse(); // 列表前后倒置

};
#include "List_implementation.h"

#endif // DATASTRUCTURE_LIST_H
