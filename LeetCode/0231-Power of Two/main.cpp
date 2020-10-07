//
// Created by 薛智钧 on 2020/4/8.
//

// Given an integer, write a function to determine if it is a power of two.


// 如果一个数是2的次方数的话，那么它的二进数必然是最高位为1
// 此时如果我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0
bool isPowerOfTwo(int n) {
    return (n > 0 && !(n & (n - 1)));
}
