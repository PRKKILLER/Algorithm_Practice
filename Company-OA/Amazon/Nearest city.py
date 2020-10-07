"""  
Amazon has centers in multiple cities. The cities are arranged on a graph, each city is located at an integral [x,y] coord
City names and locations are given the form of three arrays:c,x,andy, which are aligned by the index too provide the city name
(c[i]), and its coordinates, (x[i], y[i])

Write an algorithm to determine the name of the nearest city that shares either an x or y coordinates with the queried city. If
no other cities share an x or y coord, return NONE. If tow cities have the same distance to the queried city, return the alphabetically
smaller as the closest choice.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y

Input:
numOfCities: int
cities: a list of strings representing the names of each city[i]
xCoord: a list of integers representing the X coord of each city[i]
yCoord: a list of integers representign the Y coord of each city[i]
numOfQuires, an integer representing the number of queries
queries, a list of strings representing the names of the queried cities

Output:
Return a list of strings representign the name of the nearest city that shares either an x or a y coord with the quired city

Examples:
input:
numOfCities = 3
cities = ['c1','c2','c3']
xCoord = [3,2,1]
yCoord = [3,2,3]
numOfQueries = 3
queries = ['c1','c2','c3']

output:
[c3,None,c1]

"""
from typing import List



# def solution(numOfCities: int, cities: List[str], xCoord: List[int], yCoord: List[int], 
#                 numOfQueries: int, queries: List[str]) -> List[str]:
#     xCoord = sorted([(x, idx) for idx, x in enumerate(xCoord)], key=lambda item: item[0])
#     yCoord = sorted([(y, idx) for idx, y in enumerate(yCoord)], key=lambda item: item[0])

#     for city in queries:
#         idx = cities.index(city)


def getDistance(x1,y1,x2,y2):
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

def result(numOfCities: int, cities: List[str], xCoordinates: List[int], yCoordinates: List[int], 
                numOfQueries: int, queries: List[str]):
    result = []
    d={city: idx for idx, city in enumerate(cities)}
    
    def getNeighbors(queryCity):
        finalindex = -1
        minDist = float("inf")
        idx = d[queryCity]
        x = xCoordinates[idx]
        y = yCoordinates[idx]

        for i in range(numOfCities):
            if i != idx and (xCoordinates[i] == x or yCoordinates[i] == y) :
                distance = getDistance(x, y, xCoordinates[i], yCoordinates[i])
                if distance < minDist:
                    minDist = distance
                    finalindex = i
                elif distance == minDist:
                    if cities[i] < cities[finalindex]:
                        finalindex = i
        return finalindex
    
    for city in queries:
        temp = getNeighbors(city)
        if temp == -1:
            result.append(None)
        else:
            result.append(cities[temp])
    
    return result

numOfCities = 3
cities = ['c1','c2','c3']
xCoord = [3,2,1]
yCoord = [3,2,3]
numOfQueries = 3
queries = ['c1','c2','c3']

print(result(numOfCities, cities, xCoord, yCoord, numOfQueries, queries))





