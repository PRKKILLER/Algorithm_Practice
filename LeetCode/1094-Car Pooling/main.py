"""  
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] 
contains information about the i-th trip: the number of passengers that must be picked up, 
and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off 
all passengers for all the given trips. 


Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """  
        通过观察题目的限制条件，0 <= trips[i][1] < trips[i][2] <= 1000
        我们可以想到用 bucket sort，这是一个 O(N) 的排序算法，但是需要事先知道数据的范围

        adding passenger count to the start location, and removing it from the end location. 
        After processing all trips, a positive value for the specific location tells 
        that we are getting more passengers; negative - more empty seats.
        """

        buckets = [0] * 10001
        for t in trips:
            buckets[t[1]] += t[0]
            buckets[t[2]] -= t[0]

        for count in buckets:
            capacity -= count
            if capacity < 0:
                return False

        return True
