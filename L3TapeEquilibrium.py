def solution(A):
    sumA=0
    sumB=0
    minDiff = 100000000
    for i in range(len(A)):
        sumB = sumB + A[i]
    for i in range(len(A)-1):
        sumA = sumA + A[i]
        sumB = sumB - A[i]
        diff = abs(sumB-sumA)
        if diff < minDiff:
            minDiff = diff
    return minDiff
