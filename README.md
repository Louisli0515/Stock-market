# Stock-market-
Mainly focusing on Elliott's Wave Theory to help determining the market trend

- [Stock-market-](#stock-market-)
  * [Introduction](#introduction)
  * [Basic formation](#basic-formation)
  * [Basic principle](#basic-principle)
  * [Number the waves](#number-the-waves)
  * [Calculation of the waves](#calculation-of-the-waves)



## Introduction
Elliott Wave Theory is a technical analysis used to describe price movements in the financial market. The stock price movements and consumer behaviors can be identified as waves according to Elliot.

## Basic formation
![CI_Elliot_wave](https://user-images.githubusercontent.com/128298224/226378393-fdaabf64-d22a-4be3-a462-f33a21a456a2.jpg)


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

![WC2](https://user-images.githubusercontent.com/128298224/226394874-f9d12b75-6d73-4a94-a082-c36bae7cb931.png)

Here, Wave (1) consists of Wave (i), (ii), (iii), (iv), (v); Wave (2) consits of Wave (a), (b) and (c);... These will usually happen when you look at different time scales.

## Calculation of the waves
The calculation of prices usually involves Fibonacci Sequence.
* %Wave 2 = (Wave 1) $^{0.5}$ or (Wave 1) $^{0.618}$. Here is the Python code below which helps you calculate:

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
The above is in Bull market, the Bear market follows the similar code and will be provided in the file.

* %Wave 3 = (Wave 1) $^{1.618}$ or (Wave 1) $^{2}$ or (Wave 1) $^{2.618}$. Here is the Python code below which helps you calculate:

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
