#!/bin/python3

import math
import os
import random
import re
import sys


def filledOrders(order, k):
    order.sort()
    ans = 0
    for x in order:
        if x <= k:
            ans += 1
            k -= x
        else:
            break
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)

    fptr.write(str(result) + '\n')

    fptr.close()
