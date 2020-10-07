//
// Created by 薛智钧 on 2020/3/14.
//

#ifndef DATASTRUCTURE_STACK_SHUFFLING_H
#define DATASTRUCTURE_STACK_SHUFFLING_H

#include <stack>
#include <vector>
using namespace std;

/*
 * 思路：再来一次栈混洗，看能不能实现序列B中的效果。（设A为输入栈，B为要验证的栈）

 * 先将要验证的栈B转移到栈rb，这样B的栈底就位于rb的栈顶了，让我们可以知道依次放入栈B的元素是哪些。
 * 模拟混洗的过程，如果rb栈顶与s中一样，那么就将rb和s都pop。
 * 如果s为空，则表示能实现栈B这样一个结果。
 */

template <typename T>
bool is_stackShuffling(stack<T> A, stack<T> B){
    // rB是B的逆序，这样B的栈底就在rB的栈顶，因此就知道了B的入栈顺序
    // s作为中间段额转移栈
    stack<T> rB, s;
    while (B.size()) {
        rB.push(B.top());
        B.pop();
    }

    while (A.size()) {
        s.push(A.top());
        A.pop();

        if (s.top() == rB.top()) {
            s.pop();
            rB.pop();
            while (s.size() && s.top() == rB.top()) {
                s.pop();
                rB.pop();
            }
        }
    }
    return s.empty();
}


#endif //DATASTRUCTURE_STACK_SHUFFLING_H
