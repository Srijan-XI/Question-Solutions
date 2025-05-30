<<<<<<< HEAD
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


def minOperations(arr, threshold, d):
    # dp[i] := [count of i values, number of steps]
    dp = defaultdict(lambda: [0, 0])
    arr.sort()
    ans = sys.maxsize
    for x in arr:
        steps = 0
        while True:
            dp[x][0] += 1
            dp[x][1] += steps
            if dp[x][0] >= threshold:
                ans = min(ans, dp[x][1])
            if x == 0:
                break
            x //= d
            steps += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')

=======
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


def minOperations(arr, threshold, d):
    # dp[i] := [count of i values, number of steps]
    dp = defaultdict(lambda: [0, 0])
    arr.sort()
    ans = sys.maxsize
    for x in arr:
        steps = 0
        while True:
            dp[x][0] += 1
            dp[x][1] += steps
            if dp[x][0] >= threshold:
                ans = min(ans, dp[x][1])
            if x == 0:
                break
            x //= d
            steps += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')

>>>>>>> 81a3e0363811599296f087b9decd88efc659c78a
    fptr.close()