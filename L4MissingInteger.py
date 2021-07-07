def solution(A):
    arr = [0] * 3000000
    answer = 1
    for i in range(len(A)):
        if arr[A[i]] == 0:
            arr[A[i]] = 1
    for i in range(len(arr)):
        if i != 0 and arr[i] == 0:
            answer = i
            break
    return answer
