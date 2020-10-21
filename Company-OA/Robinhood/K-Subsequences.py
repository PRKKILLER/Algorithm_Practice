"""  
You are given an array of positive and/or negative integers and a value K . 
The task is to find count of all sub-arrays whose sum is divisible by K?

Examples :

Input  : arr[] = {4, 5, 0, -2, -3, 1}, 
         K = 5

Output : 7
// there are 7 sub-arrays whose is divisible by K
// {4, 5, 0, -2, -3, 1}
// {5}
// {5, 0}
// {5, 0, -2, -3}
// {0}
// {0, -2, -3}
// {-2, -3}
"""

def subCount(arr, n, k): 

    # create auxiliary hash 
    # array to count frequency 
    # of remainders 
    mod =[] 
    for i in range(k + 1): 
        mod.append(0) 
    
    # Traverse original array 
    # and compute cumulative 
    # sum take remainder of this 
    # current cumulative 
    # sum and increase count by 
    # 1 for this remainder 
    # in mod[] array 
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + arr[i] 

        # as the sum can be negative, 
        # taking modulo twice 
        mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1

    
    result = 0  # Initialize result 

    # Traverse mod[] 
    for i in range(k): 
    
        # If there are more than 
        # one prefix subarrays 
        # with a particular mod value. 
        if (mod[i] > 1): 
            result = result + (mod[i]*(mod[i]-1))//2

    # add the elements which 
    # are divisible by k itself  
    # i.e., the elements whose sum = 0 
    result = result + mod[0] 

    return result

arr = [4, 5, 0, -2, -3, 1] 
k = 5
n = len(arr) 

print(subCount(arr, n, k)) 