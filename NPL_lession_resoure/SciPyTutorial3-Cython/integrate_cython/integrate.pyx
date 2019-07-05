# cython: language_level=3

cdef double f_cy3(double x):
    return x ** 2 - x

def integrate_f_cy3(double a, double b, int N):
    cdef double s, dx
    cdef int i
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_cy3(a + i * dx)
    return s * dx