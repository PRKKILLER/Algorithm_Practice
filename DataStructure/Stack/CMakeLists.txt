#cmake_minimum_required(VERSION 3.15)
#project(Stack)
#
#set(CMAKE_CXX_STANDARD 11)

#set(SRC_LIST ListNode.h List.h List_implementation.h ListNode_implementation.h main.cpp)
# 注: 当应用到add_executable的SRC_LIST只有头文件时，编译器无法判断用于编译的语言，会报错
set(SRC_LIST_S main.cpp stack_list.h stack_shuffling.h)
add_executable(stack ${SRC_LIST_S})