def solution(A):
    count = 0
    sum = [0] * (len(A) + 1)
    for i in range(1, len(A)+1):
        sum[i] = sum[i-1] + A[i-1]
    for i in range(1, len(sum)):
        if(sum[i] - sum[i-1] == 1):
            cars = (i-1)-sum[i-1]
            count = count + cars
    if(count>1000000000):
        return -1
    return count
