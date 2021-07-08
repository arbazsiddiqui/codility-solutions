def solution(A):
    arrSet = set()
    max = 0
    for i in range(len(A)):
        arrSet.add(A[i])
        if(max < A[i]):
            max = A[i]
    if len(arrSet) != max:
        return 0
    if len(arrSet) != len(A):
        return 0
    return 1
