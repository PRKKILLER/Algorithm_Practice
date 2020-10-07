#set(SRC_LIST_BINTREE main.cpp BinNode.h BinTree.h)
aux_source_directory(. SRC_LIST_BINTREE)
#include_directories("../List")
add_executable(bintree ${SRC_LIST_BINTREE})