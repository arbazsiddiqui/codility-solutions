def solution(X, Y, D):
    distance_to_cover = Y - X
    q, r = divmod(distance_to_cover, D)
    if(r != 0):
        return q+1
    else:
        return q
