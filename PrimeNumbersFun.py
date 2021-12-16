from math import *
import time


def checkIfDividedByThree(num):
    num1 = str(num)
    sum = 0
    for n in num1:
        sum += int(n)
    if sum % 3 == 0:
        return True
    else:
        return False


def isPrimeHighestSpeed(a):
    if a == 2:
        return True
    i = 3
    b = sqrt(a)
    if a % 2 == 0:
        return False
    checkIfDividedByThree(a)
    while i <= b:
        if a % i == 0:
            return False
        i += 2
    return True


def isPrimeHighSpeed(a):
    if a == 2:
        return True
    i = 3
    b = sqrt(a)
    if a % 2 == 0:
        return False
    while i <= b:
        if a % i == 0:
            return False
        i += 2
    return True


def isPrimeMidSpeed(a):
    i = 2
    b = sqrt(a)
    while i <= b:
        if a % i == 0:
            return False
        i += 1
    return True


def isPrimeLowSpeed(a):
    i = 2
    while i < a:
        if a % i == 0:
            return False
        i += 1
    return True


def findSimpleUntil(until, mode):
    b = []
    i = 1
    while i < until:
        if mode == 1 and isPrimeLowSpeed(i):
            b.append(i)
        elif mode == 2 and isPrimeMidSpeed(i):
            b.append(i)
        elif mode == 3 and isPrimeHighSpeed(i):
            b.append(i)
        elif mode == 4 and isPrimeHighestSpeed(i):
            b.append(i)
        i += 1
    return b


a = 1000000
# commented because take too much time to count
# start_time = time.time()
# findSimpleUntil(a, 1)
# print("--- %s seconds Low Speed math---" % (time.time() - start_time))

start_time = time.time()
findSimpleUntil(a, 2)
print("--- %s seconds Mid Speed math---" % (time.time() - start_time))

start_time = time.time()
findSimpleUntil(a, 3)
print("--- %s seconds High Speed math---" % (time.time() - start_time))

start_time = time.time()
findSimpleUntil(a, 4)
print("--- %s seconds Highest Speed math---" % (time.time() - start_time))
