/*
You are driving a vehicle that has capacity empty seats initially available for
passengers. The vehicle only drives east (ie. it cannot turn around and drive
west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location]
contains information about the i-th trip: the number of passengers that must be
picked up, and the locations to pick them up and drop them off. The locations
are given as the number of kilometers due east from your vehicle's initial
location.

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
*/

#include <algorithm>;
#include <array>;
#include <iostream>;
#include <map>;
#include <queue>;

using namespace std;

class Solution {
 public:
  bool carPooling(vector<vector<int>>& trips, int capacity) {
    /*
    we can view this problem as meeting rooms 3.
    We use map to keep track of every timestamps, when passengers get in,
    we add passenger count; when passenger tookoff, we remove passenger count
    */
    map<int, int> mp;
    for (auto t : trips) {
      mp[t[1]] += t[0];
      mp[t[2]] -= t[0];
    }

    for (auto it : mp) {
      if ((capacity -= it.second) < 0) {
        break;
      }
    }
    return capacity >= 0;
  }

  bool carPooling(vector<vector<int>>& trips, int capacity) {
    /*
    通过观察题目的限制条件，0 <= trips[i][1] < trips[i][2] <= 1000
    我们可以想到用 bucket sort，这是一个 O(N)
    的排序算法，但是需要事先知道数据的范围

    adding passenger count to the start location, and removing it from the
    end location. After processing all trips, a positive value for the specific
    location tells that we are getting more passengers; negative - more empty
    seats.
    */

    int buckets[1001] = {};
    for (auto t : trips) {
      buckets[t[1]] += t[0];
      buckets[t[2]] -= t[0];
    }

    for (int idx = 0; capacity >= 0 && idx < 1001; ++idx) {
      capacity -= buckets[idx];
    }

    return capacity >= 0;
  }

  bool carPooling(vector<vector<int>>& trips, int capacity) {
    // sort the trips based on the beginning station
    sort(trips.begin(), trips.end(),
         [](vector<int>& a, vector<int>& b) { return a[1] < b[1]; });

    // construct min_heap to keep track of earliest tookoff passengers
    auto cmp = [](vector<int>& a, vector<int>& b) { return a[2] > b[2]; };
    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);

    for (auto t : trips) {
      // if next trip didn't have overlap with previous one
      // restore capacity
      while (!pq.empty() && pq.top()[2] <= t[1]) {
        capacity += pq.top()[0];
        pq.pop();
      }
      // update capacity
      capacity -= t[0];
      if (capacity < 0) {
        break;
      }
      pq.push(t);
    }

    return capacity >= 0;
  }
};
