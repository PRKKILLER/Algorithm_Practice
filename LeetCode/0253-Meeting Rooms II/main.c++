/*
Given an array of meeting time intervals intervals where intervals[i] = [starti,
endi], return the minimum number of conference rooms required.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
*/

#include <algorithm>;
#include <array>;
#include <iostream>;
#include <map>;
#include <queue>;

using namespace std;

class Solution {
 public:
  int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) {
      return 0;
    }

    // sort the array based on the beginning of the meetings
    sort(intervals.begin(), intervals.end(),
         [](vector<int>& a, vector<int>& b) { return a[0] < b[0]; });

    // initialize min_heap
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(intervals[0][1]);

    for (int i = 1; i < intervals.size(); ++i) {
      if (intervals[i][0] < pq.top()) {
        // if there are overlaps betweens meetings, room + 1
        pq.push(intervals[i][1]);
      } else {
        pq.pop();
        pq.push(intervals[i][1]);
      }
    }

    return (int)pq.size();
  }

  /*
    Method using map
   */
  int minMeetingRooms2(vector<vector<int>>& intervals) {
    map<int, int> mp;
    // map's key value was sorted in ascending order
    for (auto& inter : intervals) {
      ++mp[inter[0]];
      --mp[inter[1]];
    }

    int res = 0, cur = 0;
    for (auto& it : mp) {
      cur += it.second;
      res = max(res, cur);
    }

    return res;
  }
};
