import sys


def buyMaximumProducts(n, k, a):

    stocks = 0

    for i in range(1,n+1):

        if arr[i-1] >= 1 and arr[i-1]<=100 and k>=1 and k <= int(1e12):

            if a[i-1]*i <= k:

                k = k - a[i-1]*i
                print("You just bought " + str(i) + " stocks of share of price " + str(a[i-1]))
                print("Remaining : " + str(k))
                stocks += i
                print("Current Stock Pile: "+str(stocks))

            else:
                print("Can't buy all stocks!!")
                j = i-1

                while(j>=1):

                    if arr[i-1]*j > k:
                        j -= 1

                    else:
                        print("You can only buy " + str(j) + " stocks of price "+ str(arr[i-1]))
                        stocks += j
                        #k = k - a[i-1]*j
                        #print("NOTE :  Final k value : " + str(k))
                        break

                break
        else:

            return None

    return stocks



# Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())

    if n>=1 and n<= 100000:
        result = buyMaximumProducts(n, k, arr)
        print(result)
    else:
        print(None)