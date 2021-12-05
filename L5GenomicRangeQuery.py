def solution(S, P, Q):
    map = [None] * (len(S) + 1)
    charMap = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    map[0] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i, char in enumerate(S):
        if (i == 0):
            prevCount = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        else:
            prevCount = map[i]
        newCount = dict(prevCount)
        newCount[char] = prevCount[char] + 1
        map[i + 1] = newCount

    result = [0] * len(P)
    for i in range(len(P)):
        startCount = map[P[i]]
        endCount = map[Q[i] + 1]
        if (P[i] == Q[i]):
            result[i] = charMap[S[P[i]]]
        if (startCount['A'] - endCount['A'] != 0):
            result[i] = charMap['A']
        elif (startCount['C'] - endCount['C'] != 0):
            result[i] = charMap['C']
        elif (startCount['G'] - endCount['G'] != 0):
            result[i] = charMap['G']
        elif (startCount['T'] - endCount['T'] != 0):
            result[i] = charMap['T']
    return result
