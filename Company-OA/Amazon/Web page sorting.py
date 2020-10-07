"""  
Amazon's website contains one to many items in each page. To mimic the logic of the website, an programmer has a list
of items and each item has its name, relevance and price. After sorting the items by (name: 0, relevance: 1, price: 2), 
the programmer is trying to find out a list of items to displayed in a chosen page.

Given a list of items, the sort column, the sort order (0: ascending, 1: descending), the number of items to be displayed 
in each page and a page number, write an algorithm to determine the list of item names in the specified page while respecting 
the item's order (page number starts at 0)

Input:
numOfItems: an integer representing the number of items
items: a map of string as key representing the name and pair of integers as values representing the relevance, price
sortParameter, an integer representing the value used for sorting(0: name, 1: relevance, 2: price)
sortOrder, an integer representing the order of sorting(0: ascending, 1: decanding)
itemsPerPage, an integer representing the nubmer of items per page
pageNumber, an integer representing the page number to display item names(it is always less than 10)

Output:
Return a list of strings representing the item names on the requested page in the order they are displayed

Constraints:
0 <= pageNumber < 10

itemsPerPage is always greater than 0 and is always less than the minimum of numOfItems and 20

Example:
numOfItems = 3
items = [['item1',10,15],['item2',3,4],['item3',17,8]]
sortParameter = 1
sortOrder = 0
itemsPerPage = 2
PageNumber = 1

Output: ['item3']
"""

from typing import List

def solution(numOfItems, items: List[List], sortParameter, sortOrder, itemsPerPage, pageNumber) -> List[str]:
    if sortOrder == 0:  # 升序
        items = sorted(items, key=lambda x: x[sortParameter])
    elif sortOrder == 1: # 降序
        items = sorted(items, key=lambda x: x[sortParameter], reverse=True)
    
    start = itemsPerPage * pageNumber
    num = min(len(items) - start, itemsPerPage)

    res = items[start : start+num]
    return [x[0] for x in res]

numOfItems = 3
items = [['item1',10,15],['item2',3,4],['item3',17,8]]
sortParameter = 1
sortOrder = 1
itemsPerPage = 2
PageNumber = 1

print(solution(numOfItems, items, sortParameter, sortOrder, itemsPerPage, PageNumber))
