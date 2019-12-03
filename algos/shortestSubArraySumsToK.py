#fails if any A[i] < 0

def shortestSubarray(A, K):
    currWindow = [0,0]
    currSum = 0
    bestLength = 1000000
    # sums = [0]
    # for a in A:
    #     sums.append(sums[-1] + a)
    # del sums[0]
    for i in range(0,len(A)):
        #if this takes sum to negative
        currSum+=A[i]
        if currSum <= 0:
            currWindow = [i+1,i+1] 
            currSum = 0
        else:
            currWindow[1] = i
            if currSum >= K:
                while currSum - A[currWindow[0]] >= K:
                    currSum -= A[currWindow[0]]
                    currWindow[0] += 1
                bestLength = min(bestLength, currWindow[1] - currWindow[0])
    return bestLength+1

A = [1,3,1,1,9,-2,6,7]
K = 13

print(shortestSubarray(A,K))