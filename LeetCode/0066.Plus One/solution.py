class Solution:
    '''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example: input = [1,2,3] -> output = [1,2,4]

    # Special notice: python的append方法是mutate方法，是modify the list in-place, 没有返回值。
    # 即不会返回新的list
    # 若想要有返回值/返回新的一个list，可用'+'

    '''
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        n = len(digits) - 1
        while n >= 0:
            num = (digits[n] + carry) % 10
            carry = (digits[n] + carry) // 10
            digits[n] = num
            if carry == 0:
                return digits
            n -= 1

        return [1] + [0] * len(digits) # 如果到了最高位进位仍然存在，那么我们必须重新new一个数组，然后把第一个为赋成1

print(Solution().plusOne([9,9,9]))