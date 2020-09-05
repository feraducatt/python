def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1, 0-1, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
            if j == 0:
                A[j] = curNum
    return A



currNum = 1

print(insertion_sort([2, 3, 4, 6, 9,1]))


