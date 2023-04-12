from stringprep import in_table_a1


def high_low(x,y):
    p1 = x**(0.125)*y**(0.875)
    p2 = x**(0.236)*y**(0.764)
    p3 = x**(0.382)*y**(0.618)
    p4 = x**(0.5)*y**(0.5)
    p5 = x**(0.618)*y**(0.382)
    p6 = x**(0.764)*y**(0.236)
    p7 = x**(0.875)*y**(0.125)
    return p1,p2,p3,p4,p5,p6,p7
x = float(input("Enter the maxima" + " "))
y = float(input("Enter the minima" + " "))
result = high_low(x,y)
print(str(result))