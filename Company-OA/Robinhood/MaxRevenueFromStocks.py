"""  

"""


def solution(prices, algo, k):
    revenue = 0

    for i in range(len(prices)):
        if algo[i] == 0:
            revenue -= prices[i]
        else:
            revenue += prices[i]
    
    revenue_list = [revenue]

    for i in range(len(prices) - k + 1):
        revenue = 0
        for j in range(len(prices)):
            if j >= i and j < i + k or algo[j] == 1:
                revenue += prices[j]
            else:
                revenue -= prices[j]
        revenue_list.append(revenue)
    
    return max(revenue_list)

prices = [2,4,1,5,2,6,7]
algo = [0,1,0,0,1,0,0]
k = 4

print(solution(prices, algo, k))