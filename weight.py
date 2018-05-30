import math

def weight(ab,bc,ac):
    
    x=ab
    y=bc
    z=ac
    float(x)
    float(y)
    float(z)
    k= x/y
    
    a= math.sqrt(k)

    b= x/a

    c= z/a

    print a,b,c
    
    return (a+b+c)
    
x=weight(5,3,8)
print x
