#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
car=[]
truck=[]
bus=[]
bike=[]
total=0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    #word, count = line.split('\t', 1)
    word = line.split('\t')
    count = 1
    total=total+1
    car.append(int(word[2]))
    truck.append(int(word[3]))
    bus.append(int(word[4]))
    bike.append(int(word[5]))
#Prediction for car
x = range(1,len(car)+1)
def var(X):
    S = 0.0
    SS = 0.0
    for x in X:
        S += x
        SS += x*x
    xbar = S/float(len(X))
    return (SS - len(X) * xbar * xbar) / (len(X) -1.0)

def cov(X,Y):
    n = len(X)
    xbar = sum(X) / n
    ybar = sum(Y) / n
    return sum([(x-xbar)*(car-ybar) for x,car in zip(X,Y)])/(n-1)


def beta(x,car):
    return cov(x,car)/var(x)
car_pred=float((sum(car)/len(car))+beta(x,car))
print car_pred

#prediction for truck
x = range(1,len(truck)+1)
def var(X):
    S = 0.0
    SS = 0.0
    for x in X:
        S += x
        SS += x*x
    xbar = S/float(len(X))
    return (SS - len(X) * xbar * xbar) / (len(X) -1.0)

def cov(X,Y):
    n = len(X)
    xbar = sum(X) / n
    ybar = sum(Y) / n
    return sum([(x-xbar)*(truck-ybar) for x,truck in zip(X,Y)])/(n-1)


def beta(x,truck):
    return cov(x,truck)/var(x)
truck_pred=float((sum(truck)/len(truck))+beta(x,truck))
print truck_pred

#prediction for bus
x = range(1,len(bus)+1)
def var(X):
    S = 0.0
    SS = 0.0
    for x in X:
        S += x
        SS += x*x
    xbar = S/float(len(X))
    return (SS - len(X) * xbar * xbar) / (len(X) -1.0)

def cov(X,Y):
    n = len(X)
    xbar = sum(X) / n
    ybar = sum(Y) / n
    return sum([(x-xbar)*(bus-ybar) for x,bus in zip(X,Y)])/(n-1)


def beta(x,bus):
    return cov(x,bus)/var(x)
bus_pred=float((sum(bus)/len(bus))+beta(x,bus))
print bus_pred

#prediction for bike
x = range(1,len(bike)+1)
def var(X):
    S = 0.0
    SS = 0.0
    for x in X:
        S += x
        SS += x*x
    xbar = S/float(len(X))
    return (SS - len(X) * xbar * xbar) / (len(X) -1.0)

def cov(X,Y):
    n = len(X)
    xbar = sum(X) / n
    ybar = sum(Y) / n
    return sum([(x-xbar)*(bike-ybar) for x,bike in zip(X,Y)])/(n-1)


def beta(x,bike):
    return cov(x,bike)/var(x)
bike_pred=float((sum(bike)/len(bike))+beta(x,bike))
print bike_pred
# do not forget to output the last word if needed!
#if current_word == word:
#    print '%s\t%s' % (current_word, current_count)
