#!/usr/bin/env python3
# encoding: utf-8

def match_ends(words):
    c=0
    for e in words:
        if e[0]==e[-1]:
            c+=1
    return c


def main():
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    a="asd"
    print(a[0])


    s1=['aba', 'aa', 'bbb']
    s2 = ['xz', 'xx']
    r= sorted(s2)+sorted(s1)
    print(r)

    print('-'*30)
    b='tt'
    c=['uu']
    s1.append(b)
    print(s1)
    s1.append(c)
    print(s1)
    s1+=b
    print(s1)
    s1+=c
    print(s1)

    print(s1[0]!='aba')

    print('-' * 30)
    s3='asd .asd 233. s1'

    print(s3)



if __name__ == "__main__":
    main()