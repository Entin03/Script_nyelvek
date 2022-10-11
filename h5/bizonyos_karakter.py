#!/usr/bin/env python3
# encoding: utf-8

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    A megkapott paraméterből vissza adja azokat a karaktereket amelyek benne vannak
    az alapértermezett chars stringben,
    ha nincs benne egy karakter sem,
    akkor egy üres stringet ad vissza!
    """
    result=''

    for c in text:
        for c1 in chars:
            if c==c1:
                result+=c

    return print(result)


def main():
    valid("Barking!")                               #->"B"
    valid("KL754", "0123456789")                    #->"754"
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")     #->""


if __name__ == "__main__":
    main()