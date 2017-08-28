#!/bin/python3

from math import log, inf

def combine(conv1, conv2, logconv1, logconv2):
    ans = []
    anslog = []
    for i in range(n):
        ans.append(list())
        anslog.append(list())
        for j in range(n):
            best = 0
            bestlog = -inf
            for k in range(n):
                if logconv1[i][k] + logconv2[k][j] > bestlog:
                    bestlog = logconv1[i][k] + logconv2[k][j]
                    best = (conv1[i][k] * conv2[k][j]) % 1000000007
            ans[i].append(best)
            anslog[i].append(bestlog)
    return ans,anslog


n = int(input())
initial_money, initial_currency, target_currency, target_moves = [int(x) for x in input().split()]

conv1 = []
for _ in range(n):
    conv1.append([int(x) for x in input().split()])

logconv1 = []
for c in conv1:
    logconv1.append([-10**50 if x==0 else log(x) for x in c])

conv2 = [list([0]*n) for _ in range(n)]
for i in range(n):
    conv2[i][i] = 1

logconv2 = []
for c in conv2:
    logconv2.append([-inf if x==0 else log(x) for x in c])

while target_moves:
    if target_moves & 1:
        conv2, logconv2 = combine(conv2,conv1,logconv2,logconv1)
    conv1, logconv1 = combine(conv1,conv1,logconv1,logconv1)
    target_moves = target_moves >> 1

print((conv2[initial_currency][target_currency]*initial_money)% 1000000007)