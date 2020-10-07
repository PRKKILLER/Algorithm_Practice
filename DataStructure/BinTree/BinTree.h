//
// Created by 薛智钧 on 2020/3/24.
//

#ifndef LIST_IMPLEMENTATION_BTREE_H
#define LIST_IMPLEMENTATION_BTREE_H

#include "BinNode.h"

template <typename T> class BinTree{
protected:
    int _size; NodePos(T) _root; // 规模，根节点
    virtual int updateHeight(NodePos(T) x);
    void updateHeightAbove(NodePos(T) x); // 更新节点x及其祖先的高度
public:
    BinTree(): _size(0), _root(nullptr) {}
    ~BinTree() {if (0 < _size) remove(_root);}
    int size() const { return _size;}
    bool empty() const { return !_root;}
    NodePos(T) root() const { return _root;}
    NodePos(T) insertAsRoot (T const& e);
    NodePos(T) insertAsRc (NodePos(T) x, T const& e);
    NodePos(T) insertAsLc (NodePos(T) x, T const& e);
    // S是BinTree<T>类型指针的引用
    NodePos(T) attachAsLc (NodePos(T) x, BinTree<T>* &S); // S作为x左子树接入
    NodePos(T) attachAsRC (NodePos(T) x, BinTree<T>* &S); //S作为x右子树接入
    int remove (NodePos(T) x);
    //BinTree遍历函数，具体实现在BinNode类
    template <typename VST>
    void travLevel ( VST& visit ) { if ( _root ) _root->travLevel ( visit ); } //层次遍历
    template <typename VST> //操作器
    void travPre ( VST& visit ) { if ( _root ) _root->travPre ( visit ); } //先序遍历
    template <typename VST> //操作器
    void travIn ( VST& visit ) { if ( _root ) _root->travIn ( visit ); } //中序遍历
    template <typename VST> //操作器
    void travPost ( VST& visit ) { if ( _root ) _root->travPost ( visit ); } //后序遍历
};

#include "BinTree_implement.h"
#endif //LIST_IMPLEMENTATION_BTREE_H
