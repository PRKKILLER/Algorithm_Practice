"""  
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect 
friends.

Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
"""

from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        cnt = 0

        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, visited, i)
                cnt += 1

        return cnt

    def dfs(self, M, visited, person):
        for other in range(len(M)):
            # found an unvisited person in the current friend cycle 
            if M[person][other] == 1 and not visited[other]:
                # Start DFS on this new found person
                visited[other] = True
                self.dfs(M, visited, other)
