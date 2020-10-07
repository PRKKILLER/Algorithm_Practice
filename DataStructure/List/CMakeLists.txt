#cmake_minimum_required(VERSION 3.15)
#project(List)
#
#set(CMAKE_CXX_STANDARD 11)

#set(SRC_LIST ListNode.h List.h List_implementation.h ListNode_implementation.h main.cpp)
set(SRC_LIST List.h main.cpp)
add_executable(L ${SRC_LIST})