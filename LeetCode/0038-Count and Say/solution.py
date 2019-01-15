class Solution(object):
    '''
题意是n=1时输出字符串1；
n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；
n=3时，由于上次字符是11，有2个1，所以输出21；
n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。
n=5时, 输出：111221
依次类推，写个countAndSay(n)函数返回字符串。

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
    '''
    # 递归求解
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        # 因为要让i取到最后一个字符，并且后面还要进行i+1的操作，所以将原字符串随意加上一个‘*’字符防止溢出
        s = self.countAndSay(n - 1) + '*'
        res, count = '', 1 # res 作为返回值，count表示此时已经连续出现的相同字符的个数
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                res += str(count) + s[i]
                count = 1 # 还原count
        return res

    # 非递归
    def countAndSay_v2(self, n):
        """
            :type n: int
            :rtype: str
        """
        if n == 1:
            return '1'

        say = '11'
        for i in range(2, n):
            prev = say[0]
            count = 1
            newSay = ''
            for item in say[1:]:
                if prev == item:
                    count += 1
                else:
                    newSay += str(count) + prev
                    prev = item
                    count = 1
            newSay += str(count) + prev # 算上最后一位的计数
            say = newSay

        return say

if __name__ =='__main__':
    print(Solution().countAndSay_v2(5))



