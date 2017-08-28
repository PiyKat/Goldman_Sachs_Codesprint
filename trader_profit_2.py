#!/bin/python3

import sys



#### This problem can also be solved using recursion

def traderProfit(k, n, A):


    #def max_transaction(A):

        max_transactions_list = []

        for stock_price in A:

            max_transactions_list.append([x - stock_price if A.index(x) >= A.index(stock_price) else 0 for x in A]) # 1


        print("MAX TRANSACTIONS LIST : ", max_transactions_list)

        maximum = []


        for max_arrays in max_transactions_list:


                i = max_transactions_list.index(max_arrays)   # Day on which you buy

                for trans in max_arrays:

                    if trans != 0:

                        for iter in range(1,k): # Run for k transactions

                            j = max_arrays.index(trans) # Day on which you sell

                            #### Adding the exception cases when it is transacted on the last day

                            possible_sums = []

                            for remain_trans in max_transactions_list[j+1:]:   # Since you can only buy after the day you sell as only one transaction is available

                                        #if max_transactions_list.index(remain_trans) != j:

                                            #print(remain_trans)

                                for rem in remain_trans:

                                    if rem != 0:

                                        possible_sums.append(rem + trans)

                                #print("POSSIBLE SUMS : ",possible_sums)

                            if possible_sums != []:

                                print(possible_sums)

                                maximum.append(max(possible_sums))


        if maximum != []:

            return max(maximum)

        else:

            return 0



if __name__ == "__main__":
    q = int(input().strip())

    if q>=1 and q<=100:

        for a0 in range(q):
            k = int(input().strip())
            n = int(input().strip())
            arr = list(map(int, input().strip().split(' ')))
            result = traderProfit(k, n, arr)
            print(result)