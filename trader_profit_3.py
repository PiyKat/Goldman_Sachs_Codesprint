#!/bin/python3

import sys


def revert_dict(list_dict):

    reverted_dict = {}

    for i in list_dict.keys():

        reverted_dict[list_dict[i]] = i



def traderProfit(k, n, A):


        max_transactions_list = []


        ##### Only this problem left, after which it is solved, making this my greatest work

        for stock_price in A:

            max_transactions_list.append([x - stock_price if A.index(x) >= A.index(stock_price) else 0 for x in A])


        #print("MAX TRANSACTIONS LIST : ", max_transactions_list)

        maximum = []

        for max_arrays in max_transactions_list:


                i = max_transactions_list.index(max_arrays)   # Day on which you buy

                for trans in max_arrays:

                    if trans != 0:

                        #print("TRANS : " + str(trans))


                        for iter in range(0,k): # Run for k transactions

                            j = max_arrays.index(trans) # Day on which you sell , same problem as before, return min index in case of same numbers

                            #print("J : " + str(j) + " for TRANS : " + str(trans))


                            #### Adding the exception cases when it is transacted on the last day

                            possible_sums = []



                            if j != n-1:

                                for remain_trans in max_transactions_list[j+1:]:   # Since you can only buy after the day you sell as only one transaction is available

                                            #if max_transactions_list.index(remain_trans) != j:

                                                #print(remain_trans)

                                    for rem in remain_trans:

                                        if rem != 0:

                                            possible_sums.append(rem + trans)
                            else:

                                possible_sums.append(trans)
                                #print(possible_sums)
                                #print("POSSIBLE SUMS : ",possible_sums)

                            if possible_sums != []:

                                #print(possible_sums)

                                maximum.append(max(possible_sums))


        if maximum != [] and max(maximum) > 0:

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