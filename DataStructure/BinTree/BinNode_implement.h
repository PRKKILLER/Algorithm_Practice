//
// Created by 薛智钧 on 2020/3/26.
//

#ifndef DATASTRUCTURE_BINNODE_IMPLEMENT_H
#define DATASTRUCTURE_BINNODE_IMPLEMENT_H

#include <iostream>
#include <queue>
#include <stack>
#include "BinNode_macro.h"
#include "Trav_Pre.h"
#include "Trav_In.h"
#include "Trav_Post.h"


//统计当前节点后代总数，即以其为根的子树规模
template <typename T> int BinNode<T>::size() {
    int s = 1; // 计入本身
    if (lc) s += lc->size();
    if (rc) s += rc->size();
    return s;
}

//作为当前节点的左孩子插入二叉树
template <typename T> NodePos(T) BinNode<T>::insertAsLC(T const &e) {
    return lc = new BinNode(e, this);
}

// 作为当前节点的右孩子插入
template <typename T> NodePos(T) BinNode<T>::insertAsRC(T const &e) {
    return rc = new BinNode(e, this);
}

// 计算当前节点的直接后继（以中序遍历为基准）
template <typename T> NodePos(T) BinNode<T>::succ() {
    NodePos(T) s = this; // 保存当前节点的后继变量
    if (rc){ // 若有右孩子，则找到右子树中最左端的节点
        s = rc;
        while (HasLChild(* s))
            s = s->lc; // 最左侧节点
    } else{ // 若没有右孩子
        while (IsRChild(* s))
            s = s->parent;
        s = s->parent; // 可能为NULL
    }
    return s;
}

template <typename T>
void BinNode<T>::travPre(int change) {
    switch (change){
        case 1: // 递归版
            travPre_Recursive(this);
        case 2:
            travPre_I1(this);
        case 3:
            travPre_I2(this);
        default:
            travPre_Recursive(this);
    }
}

template <typename T>
void BinNode<T>::travIn(int change) {
    switch (change){
        case 1:

    }
}

template <typename T>
void BinNode<T>::travPost(int change) {
    switch (change){
        case 1:

    }
}

// 层次遍历
// 从上到下，从左到右
template <typename T>
void BinNode<T>::travLevel() {
    std::queue<NodePos(T)> Q;
    Q.push(this); // 根节点入栈
    while (!Q.empty()){
        NodePos(T) x = Q.front();
        std::cout << x->data << " "; // 访问当前节点
        if (HasLChild(*x)) Q.push(this->lc); // 左孩子入栈
        if (HasRChild(*x)) Q.push(this->rc); // 右孩子入栈
    }
}

#endif //DATASTRUCTURE_BINNODE_IMPLEMENT_H
