# Stock-market
Mainly focusing on Elliott's Wave Theory to help determining the market trend and golden ratios to determine price.

- [Stock-market](#stock-market)
  * [Introduction](#introduction)
  * [Basic formation](#basic-formation)
  * [Basic principle](#basic-principle)
  * [Number the waves](#number-the-waves)
  * [Calculation of the waves](#calculation-of-the-waves)
  * [Speical cases](#speical-cases)



## Introduction
Elliott Wave Theory is a technical analysis used to describe price movements in the financial market. The stock price movements and consumer behaviors can be identified as waves according to Elliot.

## Basic formation
<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/226378393-fdaabf64-d22a-4be3-a462-f33a21a456a2.jpg>


As shown in the above graph, a whole big wave consists of 8 small waves. There are two types of waves, one called **Impulse (Motive) wave** and the other called **Corrective wave**. In the above graph, wave 1,3 and 5 are **Impulse waves**, and wave 2 and 4 are **Corrective waves**. However we can see that the 5-wave trends are then corrected and reversed by 3-wave countertrends: A-B-C. 

The **Impulse wave** is not always in the upward direction and the **Corrective wave** is not always in the downward direction. That's because the definition of Impulse wave is to make a net movement in the same direction as the trend of the next-largest degree while the definition of Corrective wave is to correct the direction of the movement. For example, in the bear market shown in the following graph,
![grade9-reverse-abc-correction](https://user-images.githubusercontent.com/128298224/226387816-cdf90c0e-3cb8-46ff-bfa0-8f1a35cb1e16.png)

wave 1,3, and 5 are still **Impulse waves**, but they are moving downwards.

## Basic principle

* The movement of Wave 2 will not exceed the starting point of wave 1.
* Wave 3 is usually the longest wave, but cannot be the shortest (compared to Wave 1 and 5). 
* Wave 4 will never enter the domain of Wave 1.

## Number the waves

Sometimes a big wave can consist of a whole 5-3 wave. It will be shown as follows:

<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/226394874-f9d12b75-6d73-4a94-a082-c36bae7cb931.png>

Here, Wave (1) consists of Wave (i), (ii), (iii), (iv), (v); Wave (2) consits of Wave (a), (b) and (c);... These will usually happen when you look at different time scales.

## Calculation of the waves
The calculation of prices usually involves Fibonacci Sequence.
* %Wave 2 = (%Wave 1) $^{0.5}$ or (%Wave 1) $^{0.618}$. Here is the Python code below which helps you calculate:

```ruby
# Bull market, po4 and po5 are the most common ones (as stated above)
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
# Enter the highest value in Wave 1
x = float(input("Enter the final value" + " "))
# Enter the lowest value in Wave 1
y = float(input("Enter the initial value" + " "))
# Calculate the increasing rate of prices
pe = (x-y)/y
# Enter the value to start calculating (In this case is the highest value of Wave 1)
p1 = float(input("Enter the value you want to start" + " "))
result4 = wave_positive(x,y)
# pe is indeed greater than 0 as it is in bull market and the final value is the highest value of Wave 1
if pe > 0 and x == p1:
    print(str(result4))
```

* %Wave 3 = (%Wave 1) $^{1.618}$ or (%Wave 1) $^{2}$ or (%Wave 1) $^{2.618}$. Here is the Python code below which helps you calculate:

```ruby
# Bull market, poc11, poc12 and poc13 are the most common prices, while other prices are convenient for calculating prices compared Wavee 5 to Wave 1
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
x = float(input("Enter the final value" + " "))
y = float(input("Enter the initial value" + " "))
# rate of change = (final value - initial value)/initial value 
pe = (x-y)/y
# Enter the value to start calculating (In this case should be the lowest value in Wave 2)
p1 = float(input("Enter the value you want to start" + " "))
result2 = wave_poscor(x, y)
# pe is indeed greater than 0 as it is in bull market and the final value is not the hightest value of Wave 1
if pe > 0 and x != p1:
    print(str(result2))
```

* %Wave 4 = (%Wave 3) $^{0.382}$. Here is the Python code below which helps you calculate:

```ruby
# Bull market, po3 is the most common ones (as stated above)
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
# Enter the highest value in Wave 3
x = float(input("Enter the final value" + " "))
# Enter the lowest value in Wave 3
y = float(input("Enter the initial value" + " "))
# Calculate the increasing rate of prices
pe = (x-y)/y
# Enter the value to start calculating (In this case is the highest value of Wave 3)
p1 = float(input("Enter the value you want to start" + " "))
result4 = wave_positive(x,y)
# pe is indeed greater than 0 as it is in bull market and the final value is the highest value of Wave 3
if pe > 0 and x == p1:
    print(str(result4))
```

*  %Wave 5 = %Wave 1 or (%Wave 1) $^{0.618}$ when %Wave 3 > %Wave 1 or (%Wave 3) $^{0.236}$, (%Wave 3) $^{0.382}$ when %Wave 3 < %Wave 1. Here is the Python code below which helps you calculate:

```ruby
# Bull market, porc4, poc5 and poc7 are the most common prices.
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
x = float(input("Enter the final value" + " "))
y = float(input("Enter the initial value" + " "))
# rate of change = (final value - initial value)/initial value 
pe = (x-y)/y
# Enter the value to start calculating (In this case should be the lowest value in Wave 4)
p1 = float(input("Enter the value you want to start" + " "))
result2 = wave_poscor(x, y)
# pe is indeed greater than 0 as it is in bull market and the final value is not the hightest value of Wave 1
if pe > 0 and x != p1:
    print(str(result2))
```

* %Wave A = (%Wave 5) $^{0.5}$ or (%Wave 5) $^{0.618}$. Here is the Python code below which helps you calculate:

```ruby
# Bull market, po4 and po5 are the most common ones (as stated above)
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
# Enter the highest value in Wave 5
x = float(input("Enter the final value" + " "))
# Enter the lowest value in Wave 5
y = float(input("Enter the initial value" + " "))
# Calculate the increasing rate of prices
pe = (x-y)/y
# Enter the value to start calculating (In this case is the highest value of Wave 5)
p1 = float(input("Enter the value you want to start" + " "))
result4 = wave_positive(x,y)
# pe is indeed greater than 0 as it is in bull market and the final value is the highest value of Wave 5
if pe > 0 and x == p1:
    print(str(result4))
```

* %Wave B = (%Wave A) $^{0.382}$ or (%Wave A) $^{0.5}$ or (%Wave A) $^{0.618}$. Here is the Python code below which helps you calculate:

```ruby
# Bull market, so Wave A is corrective, and ne3, ne4 and ne5 are the most common ones (as stated above)
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
# Enter the lowest value in Wave A
x = float(input("Enter the final value" + " "))
# Enter the highest value in Wave A
y = float(input("Enter the initial value" + " "))
# Calculate the increasing rate of prices
pe = (x-y)/y
# Enter the value to start calculating (In this case is the lowest value of Wave A)
p1 = float(input("Enter the value you want to start" + " "))
result3 = wave_negative(x,y)
# pe is less than 0 as it is in bull market and the final value is the lowest value of Wave A
if pe < 0 and x == p1:
    print(str(result3))
```

* %Wave C = %Wave A or (%Wave A) $^{0.618}$ or (%Wave A) $^{1.382}$ or (%Wave A) $^{1.618}$. Here is the Python code below which helps you calculate:

```ruby
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
# Enter the lowest price of Wave A
x = float(input("Enter the final value" + " "))
# Enter the highest price of Wave A
y = float(input("Enter the initial value" + " "))
# rate of change = (final value - initial value)/initial value 
pe = (x-y)/y
# Enter the highest value of Wave C
p1 = float(input("Enter the value you want to start" + " "))
result1 = wave_negcor(x, y)
# pe is less than 0 in bull market and the final value is the highest value of Wave B
if pe < 0 and x != p1:
    print(str(result1))

``` 

Note here all the code is provided in bull market, full code including bear market will be attached in the file.

## Speical cases for Corrective Wave Patterns

### The Zig-Zag Formation

<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/231393249-4921d6c5-4f06-432a-9fed-335350b80b70.png>

* Zig-zag formations are very steep moves in price that go against the predominant trend.
* Wave $B$ is typically shortest in length compared to Waves $A$ and $C$.
* These zig-zag patterns can happen twice or even three times in a corection (2 to 3 zig-zag patterns linked together).
* Each of the waves in zig-zag patterns could be broken up into 5-wave patterns.

### The Flat Formation

<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/231397781-d119052c-dc39-4a52-bdea-7443f9fc703c.png>

* Flat formations are simple sideways corrective waves.
* The lengths of the waves are ***Generally*** equal in length, with wave $B$ reversing wave $A$'s move and wave $C$ undoing wave $B$'s move.
* ***Generally*** in above means sometimes wave $B$ can go beyond the beginning of wave $A$.

### The Triangle Formation

<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/231398454-2b407417-369d-4d75-ba88-8c8af539cba6.png>

* Triangle formations are corrective patterns that are bound by either converging or diverging trend lines.
* Triangles are made up of 5-waves that move against the trend in a sideways fashion. These triangles can be ***symmetrical***, ***descending***, ***ascending*** or ***expanding***.

## Price determination using golden ratios

* When we look at price charts over a long period of time, or a chart where the stock price has moved in a wide vertical range, the common linear price chart is not as useful as the ***semi-log*** chart.
* The semi-log chart has a logarithmic scale for the vertical axis while the time axis is still linear - hence the chart is a semi-log chart (not a ***log*** chart).

<img width = 50% height = 50% src = https://user-images.githubusercontent.com/128298224/231400722-f2973762-5ae1-4a27-b69d-79bf04bc2fa0.png>

