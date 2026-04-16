#이분법

def f(x):
    return(x**2-x-1)

def bisection_method(a,b,error):
    if f(a)*f(b) > 0:
        print("구간에서 근을 찾을 수 없습니다.")
    else:
        while (b-a)/2.0 > error:
            midpoint = (a+b)/2.0
            if f(midpoint) == 0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return(midpoint)
answer = bisection_method(1,2,0.0001)
print("x**2-x-1의 근:",answer)