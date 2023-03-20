from stringprep import in_table_a1
# Calculate wave 3 to wave 1; wave 5 to wave 3; wave C to wave A when the price falls
def wave_negcor(x,y):
    nec1 = p1 * ((1-abs(pe))**0.125)
    nec2 = p1 * ((1-abs(pe))**0.236)
    nec3 = p1 * ((1-abs(pe))**0.382)
    nec4 = p1 * ((1-abs(pe))**0.5)
    nec5 = p1 * ((1-abs(pe))**0.618)
    nec6 = p1 * ((1-abs(pe))**0.764)
    nec7 = p1 * ((1-abs(pe))**0.875)
    nec8 = p1 * (1-abs(pe))
    nec9 = p1 * ((1-abs(pe))**1.236)
    nec10 = p1 * ((1-abs(pe))**1.382)
    nec11 = p1 * ((1-abs(pe))**1.5)
    nec12 = p1 * ((1-abs(pe))**1.618)
    return nec1, nec2, nec3, nec4, nec5, nec6, nec7, nec8, nec9, nec10, nec11, nec12
# Compare wave 3 to wave 1; wave 5 to wave 3; wave C to wave A when the price increases
def wave_poscor(x,y):
    poc1 = p1 * ((1+pe)**0.236)
    poc2 = p1 * ((1+pe)**0.382)
    poc3 = p1 * ((1+pe)**0.5)
    poc4 = p1 * ((1+pe)**0.618)
    poc5 = p1 * ((1+pe)**0.764)
    poc6 = p1 * ((1+pe)**0.875)
    poc7 = p1 * (1+pe)
    poc8 = p1 * ((1+pe)**1.236)
    poc9 = p1 * ((1+pe)**1.382)
    poc10 = p1 * ((1+pe)**1.5)
    poc11 = p1 * ((1+pe)**1.618)
    poc12 = p1 * ((1+pe)**2)
    poc13 = p1 * ((1+pe)**2.618)
    return  poc1, poc2, poc3, poc4, poc5, poc6, poc7, poc8, poc9, poc10, poc11, poc12, poc13
# Compare wave 2 to wave 1; wave 4 to wave 3; wave B to wave A when the price falls in wave 1
def wave_negative(x,y):
    ne1 = p1 * ((1+abs(pe))**0.125)
    ne2 = p1 * ((1+abs(pe))**0.236)
    ne3 = p1 * ((1+abs(pe))**0.382)
    ne4 = p1 * ((1+abs(pe))**0.5)
    ne5 = p1 * ((1+abs(pe))**0.618)
    ne6 = p1 * ((1+abs(pe))**0.764)
    ne7 = p1 * ((1+abs(pe))**0.875)
    ne8 = p1 * ((1+abs(pe))**1)
    return ne1, ne2, ne3, ne4, ne5, ne6, ne7, ne8
# Compare wave 2 to wave 1; wave 4 to wave 3; wave B to wave A when the price increases in wave 1
def wave_positive(x,y):
    po1 = p1 * ((1-pe)**0.125)
    po2 = p1 * ((1-pe)**0.236)
    po3 = p1 * ((1-pe)**0.382)
    po4 = p1 * ((1-pe)**0.5)
    po5 = p1 * ((1-pe)**0.618)
    po6 = p1 * ((1-pe)**0.764)
    po7 = p1 * ((1-pe)**0.875)
    po8 = p1 * ((1-pe)**1)
    return po1, po2, po3, po4, po5, po6, po7, po8

x = float(input("Enter the final value" + " "))
y = float(input("Enter the initial value" + " "))
# rate of change = (final value - initial value)/initial value 
pe = (x-y)/y
p1 = float(input("Enter the value you want to start" + " "))
result1 = wave_negcor(x, y)
result2 = wave_poscor(x, y)
result3 = wave_negative(x,y)
result4 = wave_positive(x,y)
# If the rate of change is positive(price increases), and you want to know the price of the fixing wave, then use wave_positive  
if pe > 0 and x == p1:
    print(str(result4))
# If the rate of change is positive(price increases), and you want to know the price of the corresponding push wave, then use wave_poscor
if pe > 0 and x != p1:
    print(str(result2))
# If the rate of change is negative(price decreases), and you want to know the price of the fixing wave, then use wave_negative
if pe < 0 and x == p1:
    print(str(result3))
# If the rate of change is negative(price decreases), and you want to know the price of the corresponding fixing wave, then use wave_negcor
if pe < 0 and x != p1:
    print(str(result1))



