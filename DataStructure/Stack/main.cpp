#include <iostream>
#include <stack>

using namespace std;

void convert(stack<char>&, int, int);
bool match(const char*, int, int);
bool match_plus(const char*, int, int);
int myFind(const char*, int, char);

int main() {
//    cout << "Stack Algorithm Test！ " << endl;
//    stack<char> s; int n = 98, base = 2;
//    convert(s, n, base);
//    cout << "The number is: "<< n <<", the base is: "<< base <<endl;
//    cout << "The convert result is: ";
//    while (!s.empty()){
//        cout << s.top();
//        s.pop();  // pop() 函数是void, 无返回值
//    }
//    cout<<endl;
    char expr[] = "[(])";
    int length = sizeof(expr) / sizeof(expr[0]) - 1;
    cout<<"The expression is: "<< expr << endl;

    bool result = match_plus(expr, 0, length);
    cout<<"Whether the expression's brackets are match: ";
    if (result) cout<<"True"<<endl;
    else cout<<"False"<<endl;
    return 0;
}

/**stack的应用**/
// 将十进制数转化为以base为底的数
void convert(stack<char> &s, int n, int base){
    const char digit[] = "0123456789ABCDEF";  // 数位符号
    while (0 < n){
        s.push(digit[n % base]);  // 余数入栈
        n /= base;
    }
}

// 单种括号匹配
bool match(const char expr[], int lo, int hi){
    stack<char> s;
    for (int i = lo; i < hi; ++i) {
        if ('(' == expr[i]) s.push('('); // 要是满足if 条件，就会跳过后面的判断
        else if (!s.empty() && ')' == expr[i]) s.pop(); // 若stack不为空且遇到右括号，则pop顶部左括号
        else if (s.empty() && ')' == expr[i]) return false; // 若stack为空且遇到右括号，则返回FALSE
    }
    return s.empty();
}

// 多括号匹配
bool match_plus(const char expr[], int lo, int hi){
    if (expr == nullptr || (hi - lo) <=0) return false;

    stack<char> s;
    const char left[] = "([{"; const char right[] = ")]}";

    for (int i = lo; i < hi; ++i) {
        if (myFind(left, 3, expr[i]) != -1)
            s.push(expr[i]);
        else{
            int r_index = myFind(right, 3, expr[i]);
            int l_index = myFind(left, 3, s.top());

            if (r_index != -1 && s.empty()) return false;
            else if (r_index != -1 && !s.empty() && r_index != l_index) return false;
            else if (r_index != -1 && !s.empty() && r_index == l_index) s.pop();
        }
    }
    return s.empty();
}

int myFind(const char arr[], int l, char e){
    for (int i = 0; i < l; ++i) {
        if (arr[i] == e) return i;
    }
    return -1;
}