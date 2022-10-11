#!/usr/bin/env python3
# encoding: utf-8

def main():

    number=int(input('Adja meg az integer számot:'))
    for_number=0

    while (number>0):
        a = number % 10
        for_number = (for_number * 10) + a
        number = number // 10

    print("A fordítottja : {}".format(for_number))
    print(type(for_number))


if __name__ == "__main__":
    main()