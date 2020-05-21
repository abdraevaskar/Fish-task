#it's just a solution, piece of code
def solution(A, B):
    survivals = 0
    downstream = []
    for i in range(len(A)):
        if B[i] == 1:
            downstream.append(A[i])
            survivals += 1
        else:
            while downstream and A[i] > downstream[-1]:
                downstream.pop()
                survivals -= 1
            if not downstream:
                survivals += 1
    return survivals