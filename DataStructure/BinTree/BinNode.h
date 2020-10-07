//
// Created by 薛智钧 on 2020/3/24.
//

#ifndef DATASTRUCTURE_BTNODE_H
#define DATASTRUCTURE_BTNODE_H

#define NodePos(T) BinNode<T>*
#define stature(p) ((p) ? (p)->height : -1) // 节点高度(与空树高度=-1相统一)
typedef enum {RB_RED, RB_BLACK} RBColor; // 红黑树（节点颜色）

// 二叉树节点模板类
template <typename T> struct BinNode{
    T data; // 节点数值
    NodePos(T) parent; NodePos(T) lc; NodePos(T) rc; // 父节点，左右孩子
    int height; // 高度（通用）
    int npl; // Null Path Length (左式堆，也可直接用height代替)
    RBColor color; // 颜色（红黑树）

    // 构造函数
    BinNode():
        parent(nullptr), lc(nullptr), rc(nullptr), height(0), npl(1), color(RB_RED){}

    explicit BinNode(T e, NodePos(T) p = nullptr, NodePos(T) lc = nullptr, NodePos(T) rc = nullptr,
            int h = 0, int l = 1, RBColor c = RB_RED):
        data(e), parent(p), lc(lc), rc(rc), height(h), npl(l), color(c) {}

    // 操作接口
    int size(); //统计当前节点的后代总数，即以当前节点为根的子树规模
    NodePos(T) insertAsLC (T const&); // 作为当前节点的左孩子插入
    NodePos(T) insertAsRC (T const&); // 作为当前节点的右孩子插入
    NodePos(T) succ(); // 当前节点的直接后继（以中序遍历为基准）
    void travLevel(); // 子树层次遍历
    void travPre(int); // 子树先序遍历
    void travIn(int); // 子树中序遍历
    void travPost(int); // 子树后序遍历
    // 比较器
    bool operator< (BinNode const& bn) { return this->data < bn.data;}
    bool operator> (BinNode const& bn) { return this->data > bn.data;}
    bool operator== (BinNode const& bn) { return this->data == bn.data;}

};

#include "BinNode_implement.h"

#endif //DATASTRUCTURE_BTNODE_H
