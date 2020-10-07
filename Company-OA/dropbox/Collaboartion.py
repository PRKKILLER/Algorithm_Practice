"""  
每各员工都有一个0/1string， 代表其会不会与另外的人有交流。比如，如果0号员工的string是"100101"，意思就是说，
0号员工与0（自己），3，5号员工会有交流。
这个特征是有传递性的，也就是说，如果0和3有交流，3和9有交流，那么0和9就间接通过3有了交流。
现在公司把所有有交流的公司分成组，给你所有员工对应的的string，问最大的组的大小是多少。

给一个邻接矩阵，求最大连通分量：举个例子 input {"1011", "0100", "1010", "1001"} ,输出 3

"""

# def solution(connections):
#     return max(item.count('1') for item in connections)

def solution(collaborations):
    collaborations = [[int(c) for c in s] for s in collaborations]
    n = len(collaborations)
    visited = [False] * n
    max_team = 0

    for i in range(n):
        if not visited[i]:
            cur_team = dfs(collaborations, i, visited)
            max_team = max(max_team, cur_team)

    return max_team


def dfs(collaborations, idx, visited):
    if visited[idx]:
        return 0
    
    visited[idx] = True
    cnt = 1
    for i in range(len(collaborations)):
        if collaborations[idx][i] == 1:
            tmp = dfs(collaborations, i, visited)
            cnt += tmp

    return cnt

if __name__ == "__main__":
    test_1 = ["1011", "0100", "1010", "1001"]
    print(solution(test_1))