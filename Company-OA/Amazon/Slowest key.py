"""  
给一堆tuple, [(0,1),(0,5),(1,10)] 这样，tuple第一个是字母，0-25对应a-z,第二个是秒数。让输出时间最长的字母（只有一个）

A manufacturer is testing a new keyboard design. They are giving a typing test to a population and want to find out which key takes 
longest time to press. Given the results of a test, determine which key takes the longest to press.

Example: keyTimes=[(0,2),(1,5),(0,9),(2,15)]

Interpret each keyTimes[i][0] as an encoded character in the range ascii[a-z] where a=0,b=1,...,z=25
The second element, keyTimes[i][1] represents the time the key is pressed since the start of the test. 
In the example, key pressed, in order are 0102=abac at times 2,5,9,15.

From the start time, it took 2-0=2 to press the first key, 5-2=3 to press the second and so on.
The longest time it took to press a key was key 2 or 'c' at 15-9=6

Input:
slowestKey has the following params:
keyTimes[n][2]

Returns:
charater: the key that took the longest time to press

Constraints:
1 <= n <= 10^5
There will only be one key with the worst time
"""

def slowestKey(keyTimes):
    key = None
    longest_time = 0
    n = len(keyTimes)

    if n < 2: return chr(keyTimes[0][0] + 97)

    for i in range(n):
        start = keyTimes[i-1][1] if i != 0 else 0
        end = keyTimes[i][1]
        interv = end - start
        if interv > longest_time:
            key = keyTimes[i][0]
            longest_time = interv
    
    return chr(key + 97)


keyTimes=[(0,1),(0,3),(4,5),(5,6),(4,10)]
test_2 = [[0,2],[1,3],[0,7]]
print(slowestKey(test_2))

