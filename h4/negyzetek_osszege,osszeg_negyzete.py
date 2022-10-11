#!/usr/bin/env python3
# encoding: utf-8

def osszegnegyzet(start, stop):
    result = 0
    for i in range(start,stop+1):
        result+=i
    return result**2

def negyzetosszeg(start, stop):
    result = 0
    for i in range(start,stop+1):
        result+=i**2
    return result

def kulon(start, stop):
    a = osszegnegyzet(start,stop)
    b = negyzetosszeg(start,stop)
    result = a - b
    return result

def main():

    print(osszegnegyzet(1,10))
    print(negyzetosszeg(1,10))
    print(kulon(1,10))

    print(osszegnegyzet(1, 100))
    print(negyzetosszeg(1, 100))
    print(kulon(1, 100))


if __name__ == "__main__":
    main()