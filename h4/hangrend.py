#!/usr/bin/env python3
# encoding: utf-8
MAGAS_MGHK = 'eéiíöőüű'
MELY_MGHK = 'aáoóuú'

def hangrend(str):
    c1=0
    c2=0
    for s in str:
        for s1 in MAGAS_MGHK:
            if s==s1:
                c1+=1

        for s2 in MELY_MGHK:
            if s==s2:
                c2+=1

    if c1==0 and c2>0:
        return print('A megadott string mély hangrendű!')
    elif c2==0 and c1>0:
        return print('A megadott string magas hangrendű!')
    elif c1>0 and c2>0:
        return print('A megadott string vegyes hangrendű!')
    elif c1==0 and c2==0:
        return print('A megadott string semmilyen hangrendű!')

def hangrend1(str):
    c1=0
    c2=0
    for s in str:
        for s1 in MAGAS_MGHK:
            if s==s1:
                c1+=1

        for s2 in MELY_MGHK:
            if s==s2:
                c2+=1

    if c1==0 and c2>0:
        return print(str,'->mély')
    elif c2==0 and c1>0:
        return print(str,'->magas')
    elif c1>0 and c2>0:
        return print(str,'->vegyes')
    elif c1==0 and c2==0:
        return print(str,'->semmilyen')

def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    hangrend(words[0])
    hangrend(words[1])
    hangrend(words[2])
    hangrend(words[3])
    hangrend(words[4])
    hangrend(words[5])

    hangrend1(words[0])
    hangrend1(words[1])
    hangrend1(words[2])
    hangrend1(words[3])
    hangrend1(words[4])
    hangrend1(words[5])

if __name__ == "__main__":
    main()