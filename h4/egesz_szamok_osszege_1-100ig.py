#!/usr/bin/env python3
# encoding: utf-8

#Vegyük az egész számokat 1-től 100-ig, s számoljuk ki a számok számjegyeinek összegét.
#Például a [10, 11, 12] számjegyeinek összege 6 (1+0+1+1+1+2=6).

def szamjegyosszeg_1(start, stop):
    result = sum(list(range(start,stop+1)))
    return result

def szamjegyosszeg_2(ran):
    result = (ran * (ran+1))//2
    return result

def szamjegyosszeg_3(start, stop):
    result = 0
    li=[]
    for i in range(start, stop+1):
        li.append(str(i))

    for i in li:
        for i1 in i:
            result += int(i1)
    return result

def main():

    print(szamjegyosszeg_1(1,5))
    print(szamjegyosszeg_2(5))
    print('Egész számok összege 1-től 100-ig:',szamjegyosszeg_3(1,100))


if __name__ == "__main__":
    main()