# !/usr/bin/env python3
# encoding: utf-8

def iter_palindrom(s):
    i=0
    while i < len(s)//2:
        if s[i]!=s[len(s)-i-1]:
            return False
        i+=1
    return True

def reku_palindrom(s):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return reku_palindrom(s[1:-1])
        else:
            return False

def main():
    print('ITERATÍV MÓDSZER')
    print(iter_palindrom(input('Adja meg a stringet:')))

    print('\nRERKURZÍV MÓDSZER')
    print(reku_palindrom(input('Adja meg a stringet:')))
if __name__ == "__main__":
    main()