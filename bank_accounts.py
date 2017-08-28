#!/bin/python3

import sys


def feeOrUpfront(n,k, x, d, p):

    transaction_cost = 0

    #### First If
    if n >=1 and n<=100 :


        for payments in p:

            ### Combined if statements
            if payments>=1 and payments <= 1000 and k >=1 and k <=1000 and x>=1 and x<=100:

                transaction_cost += max([float(x * payments / 100), k])
            else:
                return None



    #### Third if
    if d >=1 and d<=100000:

        if transaction_cost > d:

            return "upfront"

        else:
            return "fee"


if __name__ == "__main__":

    q = int(input().strip())

    if q >= 1 and q<=5 :

        for a0 in range(q):

            n, k, x, d = input().strip().split(' ')
            n, k, x, d = [int(n), int(k), int(x), int(d)]
            p = list(map(int, input().strip().split(' ')))
            result = feeOrUpfront(n,k, x, d, p)
            print(result)
    else:
        print("No of transactions too large")