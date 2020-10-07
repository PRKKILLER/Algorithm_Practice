//
// Created by 薛智钧 on 2020/3/26.
//

#ifndef DATASTRUCTURE_TRAV_IN_H
#define DATASTRUCTURE_TRAV_IN_H

// 中序遍历迭代版
template <typename T>
void travIn_Recursive (NodePos(T) x){
    if (!x) return;
    travIn_Recursive(x->lc);
    std::cout << x->data << " ";
    travIn_Recursive(x->rc);
}

template <typename T>
static void goAlong (NodePos(T)x, std::stack<NodePos(T)> S){
    while (x){
        //当前节点入栈后随即向左深入，迭代至无左孩子
        S.push(x);
        x = x->lc;
    }
}

template <typename T>
void travIn_I1 (NodePos(T) x){
    std::stack<NodePos(T)> tmp; // 辅助栈
    while (true){
        goAlong(x, tmp); // 从当前节点出发，不断向左深入
        if (tmp.empty()) break;
        x = tmp.top(); tmp.pop();
        std::cout<< x->data << " "; // 弹出栈顶节点并访问
        x = x->rc; // 转向右子树
    }
}

// 适用于x是根节点
template <typename T>
void travIn_I2 (NodePos(T) x){
    while (HasLChild(*x)) x = x->lc; // 不断深入左子树
    std::cout << x->data << " "; // 访问最左端节点
    while ((x = x->succ()))
        std::cout<< x->data << " "; // 不断访问当前节点的后继
}

template <typename T>
void travIn_I3 (NodePos(T) x){
    while (true){
        if(HasLChild(*x)) // 若有左子树，则继续深入
            x = x->lc;
        else{// 否则
            std::cout<<x->data << " "; // 访问当前节点
            while (! HasRChild(*x)) {
                if ((x = x->succ()) == nullptr) return;
                else std::cout<< x->data << " ";
            x = x->rc; // 在有右分支的情况下，转向非空的右子树
            }
        }
    }
}

#endif //DATASTRUCTURE_TRAV_IN_H
