def solution(N, A):
    dict = {}
    maxCounter = 0
    maxValue = 0
    result = [0] * N
    for i in range(len(A)):
        if A[i] == N+1:
            maxCounter = maxCounter + maxValue
            maxValue = 0
            dict = {}
        else:
            if A[i] in dict:
                dict[A[i]] = dict[A[i]] + 1
            else:
                dict[A[i]] = 1
            if dict[A[i]] > maxValue:
                maxValue = dict[A[i]]
    for i in range(N):
        if i+1 in dict:
            result[i] = dict[i+1] + maxCounter
        else:
            result[i] = maxCounter
    return result
