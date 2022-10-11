#!/usr/bin/env python3

def main():
    a=''
    a += chr(50)
    a+= chr(48)
    a+= chr(50)
    a+= chr(50)
    print(a,type(a))
    print(chr(50),chr(48),chr(50),chr(50),sep='')
if __name__ == "__main__":
    main()