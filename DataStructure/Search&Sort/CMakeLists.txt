# cmake 最低版本号要求
#cmake_minimum_required (VERSION 3.0)
# 项目名称
# 名称之间不能有空格，例如: demo 1。 这样程序回报错
# 若要让名称之间有空格，需要加双引号

#project (Fibo)
#set(CMAKE_CXX_STANDARD 11)

# 设定工程的可执行文件
set (SRC_LIST_SS heap_sort_2.cpp)

# 指定生成目标
add_executable(sort ${SRC_LIST_SS})