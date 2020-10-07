//
// Created by 薛智钧 on 2020/3/14.
//
#include "RPN.h"

int main()
{
    std::string t1 = "(0!+1)*2^(3!+4)-(5!-67-(8+9))";
    std::cout << "input expression is: " << t1 << std::endl;
    std::cout << "result is: " << expressionCalculate(t1) << std::endl;
//    printPostfix(t1);

    return 0;
}
