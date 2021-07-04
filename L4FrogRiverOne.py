def solution(X, A):
    obj = {}
    for i in range(len(A)):
        if A[i] not in obj:
            obj[A[i]] = i
    if len(obj) != X:
        return -1
    return obj[max(obj, key=obj.get)]

