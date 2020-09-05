
def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, hi)

def get_pivot(A, low, hi):
    mid = (hi + low) //2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot

def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    border = low
    A[pivotIndex], A[low] = A[low], A[pivotIndex]

    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return pivotIndex

def quick_sort_alt(a_list):
    if len(a_list) < 2: return a_list
    lesser = quick_sort_alt([x for x in a_list[1:] if x <= a_list[0]])
    bigger = quick_sort_alt([x for x in a_list[1:] if x >  a_list[0]])
    return sum([lesser, [a_list[0]], bigger], [])


if __name__ == '__main__':
    A = [1,2,4,45,5,6,5,45]
    B = [1, 2, 4, 45, 5, 6, 5, 45]
    quick_sort(A)
    print(quick_sort_alt(B))
    
    print(A)
