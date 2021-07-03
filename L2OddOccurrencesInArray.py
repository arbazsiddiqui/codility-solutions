def solution(A):
    answer = 0
    for num in A:
        answer = answer ^ num
    return answer
