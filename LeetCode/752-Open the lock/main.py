from collections import deque

class Solution:
    """
    可以看作是求最短路径的问题。每一次转动都有8种可能：顺时针转动(4次)，逆时针转动(4次)
    """
    def openLock(self, deadends, target: str) -> int:
        # new hash set to store deadends
        deadends = set(deadends)
        # record visited path
        visited = set(['0000'])
        # initialize queue
        q = deque(['0000'])
        
        step = 0
        
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                
                # 将节点的未访问相邻节点加入队列
                for j in range(4):
                    up = self.plus(cur, j)
                    if not up in visited:
                        q.append(up)
                        visited.add(up)
                    
                    down = self.minus(cur, j)
                    if not down in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        
        return -1
    
    def plus(self, s, i):
        s = list(s)
        if s[i] == '9':
            s[i] = '0'
        else:
            s[i] = str(int(s[i]) + 1)
        return ''.join(s)
    
    def minus(self, s, i):
        s = list(s)
        if s[i] == '0':
            s[i] = '9'
        else:
            s[i] = str(int(s[i]) - 1)
        return ''.join(s)

if __name__ == "__main__":
    sol = Solution()
    sol.openLock(["0201","0101","0102","1212","2002"], "0202")