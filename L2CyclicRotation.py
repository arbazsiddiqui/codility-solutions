def solution(A, K):
    result = [None] * len(A)
    for i, num in enumerate(A):
        result[(i+K)%len(A)] = num
    return result
