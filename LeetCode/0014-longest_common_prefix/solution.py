class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Note:

    All given inputs are in lowercase letters a-z.
    '''

    # 解题思路： 利用了递归的思想。
    # 1. 首先将strs[0][0]作为参考(match = strs[0][0])，依次比较剩下序列
    # 2. 若strs[i][0] == match -> strs[i] = strs[i][1:]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        match = strs[0]
        if not match:
            return ''

        for i in range(1, len(strs)):
            temp = strs[i]
            if not temp or match[0] != temp[0]:
                return ''
            else:
                strs[i] = temp[1:]

        strs[0] = match[1:]
        return match[0] + self.longestCommonPrefix(strs)

    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        index = 0
        maxPrefix = ""
        for c in strs[0]:
            for s in strs[1:]:
                if len(s) <= index or s[index] != c:
                    return maxPrefix
            maxPrefix += c
            index += 1

        return maxPrefix


if __name__ == "__main":
    test = Solution().longestCommonPrefix_2
    a = ["flower", "flow", "flight"]
    print(test(a))
