import math


def merge(A, p, q, r):
    '''
    make two Ordinal sequence into one ordinal sequence
    :param A: A is the group of pair ordinal sequence
    :param p: the start of sequence1
    :param q: the end of sequence1 and start of sequence2
    :param r: the end of sequence2
    :return: A in Ordinal
    '''
    n1 = q - p + 1 # the length of array1
    n2 = r - q     # the length of array2
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 5, 7, 1, 2, 3, 6, 0]
# merge(A, 9, 12, 16)
# print(A)

def insert_sort(A, p, r):
    for i in range(p + 1, r):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def merge_with_insert_sort(A, p, r):
    if r - p > k:
        q = math.floor((p+r)/2)
        merge_with_insert_sort(A, p, q)
        merge_with_insert_sort(A, q + 1, r)
        merge(A, p, q, r)
    else:
        insert_sort(A, p, r)

k = 3
A = [5, 2, 4, 7, 1, 3, 2, 6]
merge_with_insert_sort(A, 0, len(A) - 1)
print(A)