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
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                carry, digits[i] = 1, 0
            else:
                carry, digits[i] = 0, digits[i] + 1
                break

        if carry:
            digits.insert(0, 1)

        return digits

    def plusOne(self, digits):
        # find right most digit != 9
        # add this digit by 1
        # set all the following digits to 0
        not_nine = -1
        for i in range(len(digits)):
            if digits[i] != 9:
                not_nine = i

        if not_nine != -1:
            digits[not_nine] += 1
        else:
            digits.insert(0, 1)

        # set all the following digits to 0
        for i in range(not_nine+1, len(digits)):
            digits[i] = 0

        return digits
