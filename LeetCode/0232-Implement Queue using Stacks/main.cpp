//
// Created by 薛智钧 on 2020/4/3.
//
#include <stack>
#include <vector>
#include <iostream>
using namespace std;

/*
   Implement the following operations of a queue using stacks.

   push(x) -- Push element x to the back of queue.
   pop() -- Removes the element from in front of queue.
   peek() -- Get the front element.
   empty() -- Return whether the queue is empty.

 * */

// 思路：利用两个stack,新进栈的缓存到_new,当要pop()或者peek()的时候再转移到old
class MyQueue {
private:
    stack<int> _old, _new;
public:
    /** Initialize your data structure here. */
    MyQueue() { }

    /** Push element x to the back of queue. */
    void push(int x) {
        _new.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int val = peek();
        _old.pop();
        return val;
    }

    /** Get the front element. */
    int peek() {
        shiftStack();
        return _old.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return _new.empty() && _old.empty();
    }

    void shiftStack(){
        if (!_old.empty()) return;
        while(!_new.empty()){
            _old.push(_new.top());
            _new.pop();
        }
    }
};

int main(){
    MyQueue my_queue;
    int a = 1, b = 3;
    my_queue.push(a);
    my_queue.push(b);
    cout << my_queue.pop() << endl;
    cout << my_queue.peek();
}
