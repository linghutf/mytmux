#!/usr/bin/env python
# encoding: utf-8

import sys

def calc_base(base,t,idx):
    s=0
    for i in xrange(idx):
        s+=base[i]*t[i]
    return s

def calc_tax(num):
    num-=3500
    base= [1500,3000,4500,26000,20000,25000]
    t   = [0.03, 0.1, 0.2, 0.25, 0.3,  0.35,0.45]
    tax = 0
    if num <= 1500:
        tax=num*0.03
    elif num>1500 and num<=4500:
        tax=(num-1500)*t[1]+calc_base(base,t,1)
    elif num>4500 and num<=9000:
        tax=(num-4500)*t[2]+calc_base(base,t,2)
    elif num>9000 and num<=35000:
        tax=(num-9000)*t[3]+calc_base(base,t,3)
    elif num>35000 and num<=55000:
        tax=(num-35000)*t[4]+calc_base(base,t,4)
    elif num>55000 and num<80000:
        tax=(num-55000)*t[5]+calc_base(base,t,5)
    else:
        tax=(num-8000)+t[6]+calc_base(base,t,6)
    return tax

def prorift(num):
    total = num
    tax = calc_tax(num)
    real = num - tax
    print "total:",total
    print "tax",tax
    print "real:",real

if __name__ == '__main__':
    num = int(sys.argv[1])
    prorift(num)

