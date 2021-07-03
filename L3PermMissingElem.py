def solution(A):
    sum = 0
    sumNatural = ((len(A)+1)*(len(A)+2))/2
    for num in A:
        sum = sum+num
    return int(sumNatural-sum)
