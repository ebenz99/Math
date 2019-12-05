#fails if any A[i] < 0

# def shortestSubarray(A, K):
#     currWindow = [0,0]
#     currSum = 0
#     bestLength = 1000000
#     B = [0]
#     for a in A:
#         B.append(B[-1] + a)
#     #del B[0]
#     print(B)
#     for i in range(0,len(B)):
#         #if this takes sum to negative
#         currSum=B[i]
#         # if currSum <= 0:
#         #     currWindow = [i+1,i+1] 
#         #     currSum = 0
#         # else:
#         #     currWindow[1] = i
#         if currSum >= K:
#             j = i-1
#             checksum = currSum - B[j]
#             while checksum < K:             #N^2 is adding the j > 0 condition and looping back for all possibilities
#                 j-=1
#                 checksum = currSum - B[j]
#             currWindow[0] = j+1
#             currWindow[1] = i
#             print(currWindow)
#             bestLength = min(bestLength, currWindow[1] - currWindow[0])
#     return bestLength+1

#fails on negative but is linear
# def shortestSubarray(A, K):
#     currWindow = [0,0]
#     currSum = 0
#     bestLength = 1000000
#     B = [0]
#     for a in A:
#         B.append(B[-1] + a)
#     #del B[0]
#     print(B)
#     buff = -K
#     j = 0

#     for i in range(1,len(B)):
#         buff+=(B[i] - B[i-1])
#         while buff - A[j] >= 0 and j < i:
#             buff-=A[j]
#             j+=1

#         if buff >= 0:
#             currWindow[0] = j
#             currWindow[1] = i
#             bestLength = min(bestLength, (currWindow[1] - currWindow[0]))

#     if bestLength == 1000000:
#         return -1
#     return bestLength

def shortestSubarray(A, K):
    currWindow = [0,0]
    currSum = 0
    bestLength = 1000000
    B = [0]
    for a in A:
        B.append(B[-1] + a)
    print(A)
    print(B)
    #del B[0]
    #print(B)
    buff = -K
    j = 0

    for i in range(1,len(B)):
        buff+=(B[i] - B[i-1])
        maxj = j
        oldj = j
        while j < i:
            if buff - B[j] >= 0:
                maxj = j
            j+=1

        if maxj != oldj:
            j = maxj
            buff -= B[j]
        print([maxj,i])

        if buff >= 0:
            currWindow[0] = j
            currWindow[1] = i
            bestLength = min(bestLength, (currWindow[1] - currWindow[0]))

    if bestLength == 1000000:
        return -1
    return bestLength


A = [11,47,97,35,-46,59,46,51,59,80,14,-6,2,20,96,1,18,74,-17,71]
B = [0, 11, 58, 155, 190, 144, 203, 249, 300, 359, 439, 453, 447, 449, 469, 565, 566, 584, 658, 641, 712]
K = 282

A = [1, 1, 1, 3]
K = 6

print(shortestSubarray(A,K))


# a = [59,46,51,59,80]
# print(sum(a))