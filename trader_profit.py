#!/bin/python3

import sys

def traderProfit(k, n, A):


    def max_transaction(A):

        max_transactions_list = []

        for stock_price in A:

            max_transactions_list.append([x - stock_price if A.index(x) >= A.index(stock_price) else 0 for x in A])

        print(max_transactions_list)


        max_trans = 0
        i = 0
        j = 0

        for trans_arrays in max_transactions_list:

            #print(arrays,type(arrays))

            arr_max = max(trans_arrays)

            if arr_max <= 0 :
                continue

            if arr_max > max_trans :

                max_trans = arr_max
                i = max_transactions_list.index(trans_arrays)
                j = trans_arrays.index(arr_max)


        return max_trans,i,j


    def arr_transform(A,i,j):

        return [x for x in A if A.index(x)<i or A.index(x)>j]



    max_profit = 0

    for x in range(k):

        maximum,i,j = max_transaction(A)
        max_profit += maximum
        A = arr_transform(A,i,j)

    return max_profit


    #max_profit = 0

    #print(max_transactions_list)

    #max_transactions_list = sorted(max_transactions_list)
    #return max_transactions_list

    # for i in range(k):
    #
    #     max_transact = max_transactions_list.pop()
    #     max_profit += max_transact
    #
    # return max_profit


    # for maximum in max_transactions_list:
    #
    #     temp_list = max_transactions_list.remove(maximum)
    #
    #     for rest in temp_list:
    #
    #         sum = max + rest
    #
    #         if sum > max:
    #
    #             max = sum
    #
    # for i in range(k):



    # while(k!=0):
    #
    #     for profit_array in transactions_list:
    #
    #         if
    #         max_value = max(profit_array)
    #
    #
    # return transactions_list


if __name__ == "__main__":
    q = int(input().strip())

    if q>=1 and q<=100:

        for a0 in range(q):
            k = int(input().strip())
            n = int(input().strip())
            arr = list(map(int, input().strip().split(' ')))
            result = traderProfit(k, n, arr)
            print(result)

