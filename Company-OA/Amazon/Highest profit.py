"""  
Amazon basics has several suppliers for its products. For each of the products, the stock is
represented by a list of a number of items for each supplier. As items are purchased, the supplier
raises the price by 1 per item purchased. Let's assume Amazon's profit on any single item is the same
as the number of items the supplier has left. For example. if a supplier has 4 items, Amazon's profit
on the first item sold is 4, then 3, then 2 and the profit of the last one is 1.

Given a list where each value in the list is the number of the item at a given supplier and also given the 
number of items to be ordered, write an algorithm to find the highest profit that can be generated for the 
given product.

Input: The input to the function consists of 3 args:
1. numSuppliers, an interger representing the number of suppliers
2. inventory, a list of long intergers representing the value of the item at a given supplier
3. order, a long interger representing the number of items to ve ordered.

Output:
Return a long integer representing the highest profit that can ve generated for the given product

Constraints:
1 <= numSuppliers <= 10^5
1 <= inventory[i] <= 10^5
1 <= order <= sum of inventory

Example:
Input:
numSuppliers=2, inventory=[3,5]
order=6

Output:
19 = 5+4+3*2+2*2
"""

from typing import List


"""  
O(n)算法
建一个 max(inventory) 的list，比方说[3,5]就是[0,0,1,0,1]
找到最大那个i=5开始
step1 i=5 t=5
[0,0,0,1,1,0,0,0......]
step2 i=4 t=5+4
[0,0,0,2,0,0,0,0......]
step3 i=3 t=5+4+3*2
[0,0,2,0,0,0,0,0......]
step4 i=2 t=5+4+3*2+2*2
[0,2,0,0,0,0,0,0......]
"""
def solution(numSuppliers: int, inventory: List[int], order: int) -> int:
    inventory = sorted(inventory)
    tmp = [0] * inventory[-1]

    for item in inventory:
        tmp[item-1] = item
    
    p = 1
    idx = inventory[-1] - 1
    maxProf = 0

    while order > 0:
        maxProf += min(p, order) * tmp[idx]
        order -= min(p, order)
        if order == 0:
            break

        idx -= 1
        if tmp[idx] > 0:
            p += 1
        else:
            tmp[idx] = idx + 1

    return maxProf


numSuppliers = 5
inventory = [2,8,4,10,6]
order = 20

print(solution(numSuppliers, inventory, order))