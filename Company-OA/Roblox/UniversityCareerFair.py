"""  
Given each company's arrival time and the duration they will stay, determine the maximum number of promotional 
events that can be hosted during the career fair.

arrival[arrival[0],..., arrival[n-1]]: ith element is the arrival time of the ith company
duration[duration[0],..,duration[n-1]]: an array of integers where ith element is the duration that the ith company
can stay at the career fair
"""


"""  
First sort the event according to (end_time, duration) in ascending order.
Then sweep the events with initial end = -Inf and ans = 0

if the arrival time is greater or equal to end, increment ans, update end as the end time for current event.
otherwise ignore the current event
Here is the greedy python solution:
Time complexity: O(n log n) since we have a sort
Space complexity: O(n) since I create a new list to store the sorted information, you can also sort the input list in-place so it uses O(1) space
"""
def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans