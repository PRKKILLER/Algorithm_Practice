#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    if (k == nums.size()) {
      return nums;
    }

    map<int, int> num_freq;
    for (int n : nums) {
      num_freq[n] += 1;
    }

    // custome compare function to initialzie min_heap
    auto cmp = [&num_freq](int n1, int n2) {
      return num_freq[n1] > num_freq[n2];
    };

    priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);

    for (pair<int, int> p : num_freq) {
      pq.push(p.first);
      if (pq.size() > k) {
        pq.pop();  // pop the least frequency element
      }
    }

    vector<int> res;
    for (int i = 0; i < k; ++i) {
      res.push_back(pq.top());
      pq.pop();
    }

    return res;
  }

  vector<int> topKFrequent2(vector<int>& nums, int k) {
    if (k == nums.size()) {
      return nums;
    }

    map<int, int> num_freq;
    for (int n : nums) {
      num_freq[n] += 1;
    }

    // row: frequency; col: nums with the same freq
    vector<vector<int>> buckets((int)(nums.size() + 1));
    for (pair<int, int> p : num_freq) {
      buckets[p.second].push_back(p.first);
    }

    vector<int> res;
    for (auto it = buckets.rbegin(); it != buckets.rend(); ++it) {
      if (!(*it).empty()) {
        for (int num : (*it)) {
          res.push_back(num);
          if (--k == 0) {
            return res;
          }
        }
      }
    }

    return res;
  }
};
