//
// Created by 薛智钧 on 2020/3/14.
//

#ifndef DATASTRUCTURE_RPN_H
#define DATASTRUCTURE_RPN_H

#include <iostream>
#include <string>
#include <stack>
#include <cstdlib>
#include <map>
#include <cmath>
#include "priority.h"

int fac(int n); // 阶乘计算
Operator optr2rank ( char op );  //由运算符转译出编号
char orderBetween(char op1, char op2);  //比较两个运算符的优先级
std::string infixToPostfix(const std::string& infix);  //中缀表达式 -> 后缀表达式
float postfixCompute(std::string postfix);  //后缀表达式计算
float expressionCalculate(const std::string& expr);  //计算接口
void printPostfix(const std::string& postfix);

#endif //DATASTRUCTURE_RPN_H
