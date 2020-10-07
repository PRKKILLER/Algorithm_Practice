"""  
Write an algorithm to find who in the group has the smallest negative balance. 

Input:
The input to the function/method consists of three arguments:
numRows, an integer representing the number of debt records.
numCols, an integer representing the number of elements in debt records. It is always 3.
debts, a list of triplet representing debtRecord consisting of a string borrower, a string lender, and an integer
amount, representing the debt record.

Output:
Return a list of strings representing an alphabetically ordered list of members with 
the smallest negative balance. If no team member has a negative balance then return a list containing 
the string "Nobody has a negative balance".

Constraints:
1 ≤ numRows ≤ 2*10^5
1 ≤ amount in debts ≤ 1000
1 ≤ length of borrower and lender in debts ≤ 20

Example:
Input:
numOfRows = 6
numCols = 3

debts:
borrower | lender | amount
Alex     | Blake  | 2
Blake    | Alex   | 2
Casey    | Alex   | 5
Blake    | Casey  | 7
Alex     | Blake  | 4
Alex     | Casey  | 4

Output:
['Alex', 'Blake']

First, fifth, and sixth entries decrease Alex's balance because Alex is a borrower.
Second, third increase b/c Alex is a lender.
Alex balance: (2+5) - (2+4+4) = 7 - 10 = -3
Blake is lender in first and fifth entries and a borrower in second and fourth
Blake balance: (2+4) - (2+7) = 6-9 = -3
Casey is a borrower in third entry and a lender in the fourth and sixth
Casey balance: (7 + 4) - (5) = 11 - 6 = 5
"""

from typing import List
import functools

def solution(numRows: int, numCols: int, debts: List) -> List[str]:
    people = set([item[0] for item in debts])  # 人员名单
    m = {p: 0 for p in people}

    for item in debts:
        m[item[0]] -= item[2]
        m[item[1]] += item[2]

    res = [(p, val) for p, val in m.items() if val < 0]
    if not res:
        return "Nobody has a negative balance"

    # def compare(x, y):
    #     if x[1] != y[1]:
    #         return x[1] > y[1]
    #     else:
    #         return x[0] > y[0]

    # res = sorted(res, key = functools.cmp_to_key(compare))
    res = sorted(res, key = lambda pair: (pair[1], pair[0]))
    return [item[0] for item in res]

numOfRows = 6
numCols = 3
debts = [['Alex', 'Blake', 2], ['Blake', 'Alex', 2], ['Casey', 'Alex', 5], ['Blake', 'Casey', 7],
['Alex', 'Blake', 4], ['Alex', 'Casey', 4]]

print(solution(numOfRows, numCols, debts))

