//
// Created by 薛智钧 on 2020/3/14.
//

#include "RPN.h"
using namespace std;

// 由char类型符号转义出编号
Operator optr2rank(char op){
    switch (op){
        case '+' : return ADD; //加
        case '-' : return SUB; //减
        case '*' : return MUL; //乘
        case '/' : return DIV; //除
        case '^' : return POW; //乘方
        case '!' : return FAC; //阶乘
        case '(' : return L_P; //左括号
        case ')' : return R_P; //右括号
        default  : exit ( -1 ); //未知运算符
    }
}

// 返回符号优先级
//op1: 栈顶运算符  op2: 当前运算符
char orderBetween(char op1, char op2) {
    return pri[optr2rank(op1)][optr2rank(op2)];
}

int fac(int n) {
    int f = 1;
    while (n > 1) f *= n--;
    return f;
}

string infixToPostfix(const string& infix) {
    char current = 0;
    string postfix; // 存放后缀表达式
    stack<char> optr; // 符号栈

    // 用string的const_iterator进行迭代
    for (string::const_iterator i = infix.begin(); i != infix.end(); ++i) {
        current = *i;
        switch (current) {
            case '0':case '1':case '2':case '3':case '4':case '5':
            case '6':case '7':case '8':case '9':case '.':
                postfix.push_back(current); // 数字直接写入
                break;
            case '+':case '-':case '*':case '/' :case '^':case '!':
                // 如果infix前一项不是')'或'!'，说明数字输入完成了，用#标记
                if (*(i - 1) != ')' && *(i - 1) != '!')
                    postfix.push_back('#');
                //如果符号栈非空，即比较栈顶符号与当前符号的优先级，
                //若栈顶运算符优先级 > 当前运算符,则栈顶运算符出栈(并写入输出字符串到postfix)，
                //直至符号全部出栈或者遇到了'('或者大于栈顶符号的优先级
                if (!optr.empty()) {
                    char optr_top = optr.top();
                    while (optr_top != '(' && orderBetween(optr_top, current) == '>'){
                        postfix.push_back(optr_top);
                        optr.pop();
                        if (optr.empty()) //optr栈空，跳出循环
                            break;
                        optr_top = optr.top();
                    }
                }
                //若栈顶运算符优先级 < 当前运算符 或 运算符栈为空，则将当前运算符入栈
                optr.push(current);
                break;
            case '(':
                if (*(i - 1) >='0' && *(i - 1) <='9'){ // 应对例如 2+3(3+1)的情况
                    postfix.push_back('#');
                    optr.push('*');
                }
                optr.push(current); // 左括号入栈
                break;
            case ')':
                if (*(i - 1) >= '0' && *(i - 1) <= '9')
                    postfix.push_back('#');// ')'说明前方数字完成，标记一下
                while (optr.top() != '('){
                    postfix.push_back(optr.top());
                    optr.pop();
                }
                optr.pop(); // 左括号出栈
                break;
            default:
                exit(-1); // 未知运算符
        }
    }
    if (infix[infix.size()-1] != ')' && infix[infix.size()-1] != '!')
        postfix.push_back('#');
    while (!optr.empty()){ // 若符号栈非空，写入postfix
        postfix.push_back(optr.top());
        optr.pop();
    }
    return postfix;
}


/*  计算后缀表达式结果
    输入为后缀表达式postfix，逐个读取字符，如果是数字即放入存放当前数字的字符串中，
    遇到“#”, 使用std::stof()即将此字符串转换为float，
    完成数字识别转化后入栈，遇到符号即取出栈顶的两个数字计算，结果入栈。
    栈中最后的元素即为结果。
*/
float postfixCompute(std::string postfix) {
    std::stack<float> currResult; // 入栈当前postfix计算结果
    string strNum; // 在遇到'#'标识符之前，保存str类型数据
    float currNum = 0.0; // 保存str2float转化后的结果
    float tempResult = 0.0; // 在入栈前暂存结果

    for (string::const_iterator i = postfix.begin(); i != postfix.end(); ++i) {
        switch (*i) {
            case '0':case '1':case '2':case '3':case '4':case '5':
            case '6':case '7':case '8':case '9':case '.':
                strNum.push_back(*i);
                break;
            case '#': // 当前数字结束
                currNum = stof(strNum);  //string to float
                strNum.clear();
                currResult.push(currNum);
                break;
            case '+': // 将currResult顶部两个数据出栈，进行计算
                tempResult = currResult.top();
                currResult.pop();
                tempResult += currResult.top();
                currResult.pop();
                currResult.push(tempResult);
                break;
            case '-':
                tempResult = currResult.top();
                currResult.pop();
                tempResult = currResult.top() - tempResult;
                currResult.pop();
                currResult.push(tempResult);
                break;
            case '*':
                tempResult = currResult.top();
                currResult.pop();
                tempResult *= currResult.top();
                currResult.pop();
                currResult.push(tempResult);
                break;
            case '/':
                tempResult = currResult.top();
                currResult.pop();
                tempResult = currResult.top() / tempResult;
                currResult.pop();
                currResult.push(tempResult);
                break;
            case '^':
                tempResult = currResult.top();
                currResult.pop();
                tempResult = pow(currResult.top(), tempResult);
                currResult.pop();
                currResult.push(tempResult);
                break;
            case '!':
                tempResult = currResult.top();
                tempResult = (float)fac((int)tempResult); //阶乘
                currResult.pop();
                currResult.push(tempResult);
                break;
        }
    }
    return currResult.top();
}

float expressionCalculate(const string& expr){
    return postfixCompute(infixToPostfix(expr));
}

void printPostfix(const string& expr){
    cout << "The postfix of the expression is: "
         << infixToPostfix(expr);
}
