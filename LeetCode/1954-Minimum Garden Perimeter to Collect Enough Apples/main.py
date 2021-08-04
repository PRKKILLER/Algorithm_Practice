"""  
In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer 
coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.

You will buy an axis-aligned square plot of land that is centered at (0, 0).

Given an integer neededApples, return the minimum perimeter of a plot 
such that at least neededApples apples are inside or on the perimeter of that plot.

The value of |x| is defined as:

x if x >= 0
-x if x < 0

Constraints:
1 <= neededApples <= 10^15

Example:

Input: neededApples = 1
Output: 8

distance = 1

(2) --- (1) --- (2)
 |               |               
 |               |
(1)             (1)
 |               |
 |               |
(2) --- (1) --- (2)

distance = 2

(4) --- (3) --- (2) --- (3) --- (4)
 |                               |               
 |                               |
(3)                             (3)
 |                               |
 |                               |  
(2)                             (2)
 |                               |
 |                               |    
(3)                             (3)
 |                               |
 |                               |
(4) --- (3) --- (2) --- (3) --- (4)
"""

"""  
经过观察可知，当 distance = n 时，一共有 8n 个点在 square 的边上
并且周长 = 8n

总共的 Apple 数量 = 8n * n + ((1 + n) * n / 2) * 8 - 4 * n = 12 * n^2
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        acc = 0
        d = 1
        while acc < neededApples:
            acc += 12 * (d ** 2)
            d += 1

        return 8 * (d - 1)
