# def fibo(n):
#     mylist = []
#     for i in range(n):
#         if i <= 1:
#             mylist.append(i)
#         else:
#             mylist.append(mylist[-1] + mylist[-2])
#     return mylist
#
#
# print(fibo(20))
import math


# def fibo(n):
#     fiboList = [0, 1, 1, 2]
#
#     [fiboList.append(fiboList[-1] + fiboList[-2]) for _ in range(n - len(fiboList))]
#
#     return fiboList
#
#
# fiboList = fibo(5)
# print(fiboList)
#
# squareFibo = [n**2 for n in fiboList]
# print(squareFibo)
#
# oddFibo = [n for n in squareFibo if n % 2 != 0]
# print(oddFibo)
# print(sum(oddFibo))



def fibo(n):
    fiboList = [0, 1, 1, 2]
    [None if i < 2 else fiboList.append((math.ceil(i + i*0.6))) for i in range(n - len(fiboList))]

    return fiboList

print(fibo(20))



















