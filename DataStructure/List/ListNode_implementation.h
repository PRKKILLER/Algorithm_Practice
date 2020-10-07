//
// Created by 薛智钧 on 2020/3/12.
//

#ifndef DATASTRUCTURE_LISTNODE_IMPLEMENTATION_H
#define DATASTRUCTURE_LISTNODE_IMPLEMENTATION_H


template <typename T>
NodePos(T) ListNode<T>::insertAsPred (T const& e){
    NodePos(T) x = new ListNode(e, pred, this);
    pred->succ = x;
    pred = x;
    return x;
}

template <typename T>
NodePos(T) ListNode<T>::insertAsSucc(T const& e){
    NodePos(T) x = new ListNode(e, this, succ);
    succ->pred = x;
    succ = x;
    return x;
}
#endif //DATASTRUCTURE_LISTNODE_IMPLEMENTATION_H
