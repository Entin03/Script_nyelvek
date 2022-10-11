#!/usr/bin/env python3
# encoding: utf-8

def strclean(s):
    return ''.join(s.split())
def main():

    s1='192.20.246.138:\n 6666'
    s2='206.130.99.82:\n8080';
    print(strclean(s1))
    print(strclean(s2))



if __name__ == "__main__":
    main()