def insertion_swap(A: list) -> list:
    for i in range(1,len(A)):
        j = i
        while A[j-1] > A[j] and j > 0:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A
            
print(insertion_swap([5,8,7,2,4,9,1]))