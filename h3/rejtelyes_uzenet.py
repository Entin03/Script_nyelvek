#!/usr/bin/env python3
import string


TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""".strip()


def dekodol(s):
    result = []
    kisb = string.ascii_lowercase
    nagyb = string.ascii_uppercase
    for e in s:
        if e in kisb:
            result.append(kisb[(kisb.find(e)+2)%26])
        else:
            if e in nagyb:
                result.append(nagyb[(nagyb.find(e)+2)%26])
            else:
                result.append(e)
    return ''.join(result)


def main():
    print(dekodol(TEXT))


if __name__ == "__main__":
    main()