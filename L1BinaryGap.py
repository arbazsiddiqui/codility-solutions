def solution(N):
    binary = "{0:b}".format(N)
    max_count = 0
    current_count = 0
    for char in binary:
        print(max_count, current_count)
        if char == '0':
            current_count = current_count + 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0
    return max_count
