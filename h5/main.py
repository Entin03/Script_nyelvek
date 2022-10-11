#!/usr/bin/env python3
# encoding: utf-8

def osszeg_harom_v_ot(int):
    """
    kiszámítja azon egész számok összegét a megadott paraméterig
    amelyik osztható 3-mal vagy 5-el
    """

    return sum([i for i in range(int) if i%3==0 or i%5==0])

def main():

    print(osszeg_harom_v_ot(1000))

if __name__ == "__main__":
    main()