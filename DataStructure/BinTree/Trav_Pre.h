//
// Created by 薛智钧 on 2020/3/26.
//

#ifndef LIST_IMPLEMENTATION_TRAV_PRE_H
#define LIST_IMPLEMENTATION_TRAV_PRE_H

template <typename T>
void travPre_Recursive(NodePos(T) x){
    if (!x) return;
    std::cout << x->data << " ";
    travPre_Recursive(x->lc);
    travPre_Recursive(x->rc);
}

template <typename T>
static void visitAlong (NodePos(T) x, std::stack<NodePos(T)>& S){
    while (x){
        std::cout << x->data << " "; // 访问当前节点
        if (HasRChild(*x)) S.push(x->rc); // 当前节点右孩子入栈暂存
        x = x->lc; // 继续想当前左子树移动
    }
}

template <typename T>
void travPre_I1 (NodePos(T) x){
    std::stack<NodePos(T)> tmp; // 辅助栈
    while (true){
        // 访问子树x的藤蔓各右子树的根入栈
        visitAlong(x, tmp);
        if (tmp.empty()) break;
        x = tmp.top(); // 弹出下一右子树（根）
        tmp.pop();
    }
}

template <typename T>
void travPre_I2 (NodePos(T) x){
    std::stack<NodePos(T)> tmp; // 辅助栈
    if (x) tmp.push(x); // 根节点入栈
    while (!tmp.empty()){
        x = tmp.top(); tmp.pop(); // 弹出并访问当前节点
        std::cout << x->data << " ";
        if (HasRChild(*x)) tmp.push(x->rc); // 右孩子先入后出
        if (HasLChild(*x)) tmp.push(x->lc); // 左孩子后入先出
    }
}

#endif //LIST_IMPLEMENTATION_TRAV_PRE_H