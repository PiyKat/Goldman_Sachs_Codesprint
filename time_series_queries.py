#!/bin/python3

import sys

def query_1(t,p,v):

    for x in p:

        if x < v:

            if p.index(x) == len(p) - 1:

                return -1

            else:
                continue

        elif x >= v:

            time_index = p.index(x)
            return t[time_index]

        else:
            return -1


def query_2(t,p,v):

    max_price = 0

    for x in t:

        if x < v:

            if t.index(x) == len(t) - 1:

                return -1

            else:

                continue


        elif x >= v:

            return max(p[t.index(x)])

            # for x1 in p[t.index(x):]:
            #
            #     if x1 > max_price:
            #
            #         max_price = x1
            #
            # return max_price

        else:

            return -1



if __name__ == "__main__":

    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    t = list(map(int, input().strip().split(' ')))
    p = list(map(int, input().strip().split(' ')))
    for a0 in range(q):
        _type, v = input().strip().split(' ')
        _type, v = [int(_type), int(v)]

        if _type == 1:
            print(query_1(t, p, v))
        elif _type == 2:
            print(query_2(t, p, v))
        else:
            print("Wrong Query Type")