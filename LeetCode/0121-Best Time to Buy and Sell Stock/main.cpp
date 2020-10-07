//
// Created by 薛智钧 on 2020/3/23.
//

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

/*Say you have an array for which the ith element is the price of a given stock on day i.

  If you were only permitted to complete at most one transaction
  (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

  Note that you cannot sell a stock before you buy one.

  Example 1:

  Input: [7,1,5,3,6,4]
  Output: 5
  Explanation:
  Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
  Not 7-1 = 6, as selling price needs to be larger than buying price.

 */
class Solution {
public:
    // Not pass: Time exceeded
    int maxProfit(vector<int>& prices) {
        int maxP = 0; // 记录当前最大利润值
        for (int i = 0; i < prices.size(); ++i) {
            for (int j = i; j < prices.size(); ++j) {
                int curr = prices[j] - prices[i];
                maxP = max(maxP, curr);
            }
        }
        return maxP;
    }

    // ˙支循环一次，保存 minValue 和 maxProfit
    int maxProfit_2(vector<int>& prices){
        int minValue = INT_MAX, maxprofit = 0;
        for (int price : prices){
            if (price < minValue)
                minValue = price; // 若小于当前间隔谷底，则保留
            else                  // 否则比较当前值和谷底值的差是否大于maxprofit
                maxprofit = max(price - minValue, maxprofit);
        }
        return maxprofit;
    }
};

int main(){
    vector<int> profit = {7,6,4,3,1};
    Solution sol;
    int res = sol.maxProfit_2(profit);
    cout << "Max profit is: "<< res;
}