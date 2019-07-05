double f(double x){
    return x*x-x;
}

double integrate(double a, double b, int N){
    double s, dx;
    int i;
    s = 0;
    dx = (b-a)/N;
    for(i=0; i<N; i++){
        s+=f(a+i*dx);
    }
    return s*dx;
}