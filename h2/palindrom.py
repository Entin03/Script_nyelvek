#!/usr/bin/env python3
# encoding: utf-8

def main():
    print('-----VERZIÓ1-----')
    print('Palindróm függvény')
    s=input('Adjon meg egy stringet:')
    s1 = s[::-1]
    if s==s1:
        print("A megadott string palindróm!")
    else:
        print("A megadott sring nem palindróm!")

    print('-----VERZIÓ2-----')
    str = 'as'
    str1 = str.casefold()
    rev = reversed(str)
    if list(str) == list(rev):
        print("PALINDROME !")
    else:
        print("NOT PALINDROME !")


if __name__ == "__main__":
    main()