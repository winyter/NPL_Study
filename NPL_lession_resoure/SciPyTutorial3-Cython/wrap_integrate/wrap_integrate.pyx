cdef extern from "integrate.h":
    double integrate(double a, double b, int N)

def integrate_c(double a, double b, int N):
    return integrate(a, b, N)