class Solution:
    def maximumNumber(self, num: str, change) -> str:
        res = []
        flag = True
        bigger = False
        idx = 0

        for d in num:
            if change[int(d)] > int(d) and flag:
                res.append(str(change[int(d)]))
                bigger = True
                idx += 1
            elif change[int(d)] == int(d):
                res.append(str(change[int(d)]))
                idx += 1
            elif change[int(d)] < int(d):
                if len(res) > 0 and bigger:
                    flag = False
                    break
                else:
                    idx += 1
                    res.append(d)

        res.extend(list(num[idx:]))
        return ''.join(res)


sol = Solution()
# num = "334111"
num = "5"
# change = [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]
change = [9, 3, 6, 3, 7, 3, 1, 4, 5, 8]

print(sol.maximumNumber(num, change))
