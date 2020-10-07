//
// Created by 薛智钧 on 2020/4/3.
//
#include<queue>
#include<iostream>
using namespace std;

/*
 * Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
 * */

// 思路：利用两个队列q1, q2，其中q2用来存放栈顶元素
class MyStack {
private:
    queue<int> q1, q2;
public:
    /** Initialize your data structure here. */
    MyStack() { }

    /** Push element x onto stack. */
    void push(int x) {
        q2.push(x);
        while(q2.size() > 1) { // 若q2中有多余元素，则将剩余元素顺序入q1队列
            q1.push(q2.front());
            q2.pop();
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int val = top();
        q2.pop();
        return val;
    }

    /** Get the top element. */
    int top() {
        if (q2.empty()){
            for (int i = 0; i < q1.size() - 1; ++i){
                q1.push(q1.front()); // 将q1的头部元素倒插入q1的尾部
                q1.pop();
            }
            q2.push(q1.front());
            q1.pop();
        }
        return q2.front();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

class myStack{
private:
    queue<int> q;
public:
    void push(int x){
        q.push(x);
        for (int i = 0; i < (int)q.size() - 1; ++i){
            q.push(q.front());
            q.pop();
        }
    }

    int pop(){
        int val = q.front();
        q.pop();
        return val;
    }

    int top(){
        return q.front();
    }

    bool empty(){
        return q.empty();
    }
};
