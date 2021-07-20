#include <iostream>
#include <queue>
#include <vector>

using namespace std;

/*
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Example:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just
[[-2,2]].
*/

class Solution {
 public:
  /*
  time complexity: O(N) + O(KlogN)
  O(N) part is for adding all the elements to the heap.
  O(KlogN) is for fetching the top k elements from the min heap.
  */
  vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // min heap has the smallest element at the root
    auto cmp = [](vector<int>& p, vector<int>& q) {
      return p[0] * p[0] + p[1] * p[1] > q[0] * q[0] + q[1] * q[1];
    };

    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(
        points.begin(), points.end(), cmp);
    vector<vector<int>> res;

    for (int i = 0; i < k; ++i) {
      res.push_back(pq.top());
      pq.pop();
    }

    return res;
  }

  /*
  Use max heap to maintain the k closest points to the origin.
  max heap has the biggest element at the root. Each time we add a point to the
  heap, if the size exceeds k, we pop our the root element. Finally, there are k
  smallest element in the pq

  time complexity: O(NlogK)
  */
  vector<vector<int>> kClosest2(vector<vector<int>>& points, int k) {
    // max heap
    auto cmp = [](vector<int>& p, vector<int>& q) {
      return p[0] * p[0] + p[1] * p[1] < q[0] * q[0] + q[1] * q[1];
    };

    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
    vector<vector<int>> res;

    for (vector<int>& p : points) {
      pq.push(p);
      if (pq.size() > k) {
        pq.pop();  // pop out the largest element
      }
    }

    while (!pq.empty()) {
      res.push_back(pq.top());
      pq.pop();
    }

    return res;
  }
};
