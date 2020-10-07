"""  
Design Hit Counter
Things to consider: 
1. If a lot of hits within given time window / per sec
2. Multi-threading, if multiple threads report hit #Example: if a webpage, multiple clients click hit
"""

from collections import deque

"""  
1. 简单版本，不考虑多线程
"""
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._counter = deque()
        self.th = 300
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._counter.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        cutoff = timestamp - self.th
        if self._counter and self._counter[-1] <= cutoff:
            return 0
        
        while self._counter:
            if self._counter[0] <= cutoff:
                self._counter.popleft()
            else:
                break
        
        return len(self._counter)


# python solution: O(1) Space, O(1) hit, O(S) gethits()
"""  
using a tuple and referencing the variable at the same time so even if the context switch 
happens in a multithreaded environment, both hits and times will be in sync

can achieve synchronized modification and reading
or using blocking queue

it can handle multiple hit at the same time, because this approach does not involve dynamic allocating the space
"""

class HitCounter2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.th = 300
        self.q = [(0, 0)] * self.th

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % self.th
        time, hit = self.q[idx]
        if time != timestamp:
            # previous timestamp is outdated, safe to override
            self.q[idx] = timestamp, 1
        else:
            self.q[idx] = time, hit + 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        cnt = 0
        cutoff = timestamp - self.th
        for time, hit in self.q:
            if time > cutoff:
                cnt += hit
        return cnt