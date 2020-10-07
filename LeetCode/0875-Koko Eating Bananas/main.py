"""  
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.


Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
"""

class Solution:
    """  
    分析问题可以知道，猴子每小时最多吃一个pile, 因此eating的最低speed = 1，最大speed = max(piles)
    我们需要在 [min_speed, max_speed]中找到1个恰当的speed，这就可以利用到Binary search
    每一个speed对应一个eating time，我们需要找到eating time = H 的speed，并且需要speed的值最小，
    这就演变为在一个数组中查找target=H的最小秩，数组的下标就是speed
    """
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles) + 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if self.eatTime(mi, piles) <= H:
                hi = mi
            else:
                lo = mi + 1
        
        return lo
    
    def eatTime(self, speed, piles):
        cnt = 0
        for item in piles:
            cnt += math.ceil(item / speed)
        return cnt