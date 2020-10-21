"""  
A frog is crossing a river. The river is divided into x units and at each unit there may or 
may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
"""

"""
思路：可以将该问题看作为1个tree problem，每一个node有3个children
我们从stones[0]出发，检查是否能reach stones[-1]
利用BFS，将当前stone临近的stone加入队列
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        from collections import deque
        
        end = stones[-1]
        stonesSet = set(stones)
        
        if stones[0] + 1 not in stonesSet:
            return False
        
        # 注意：visited加入的是 (pos, step)
        # frog有可能land在同一个position上，但是step不一样，那么结果也不一样
        visited = set([(stones[0] + 1, 1)])
        q = deque([[stones[0] + 1, 1]])
        
        while q:
            sz = len(q)
            for i in range(sz):
                pos, step = q.popleft()
                if pos == end:
                    return True
                elif pos < end:
                    # add current position's neighbor
                    for i in range(step-1, step+2):
                        if i < 0:
                            continue
                        
                        next_pos = pos + i
                        if next_pos in stonesSet and (next_pos, i) not in visited:
                            q.append([next_pos, i])
                            visited.add((next_pos, i))
            
        return False