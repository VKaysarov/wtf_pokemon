#cython: language_level=3
cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y

print(test(2))