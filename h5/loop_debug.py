#!/usr/bin/python python3

def loop(n, debug=False):
    """
    A megadott n paraméterig írjuk ki a számukat egytől.

    Ha a debug paramétert true-ra állítjuk,
    akkor kiírjuk azt hogy: # ciklus kedzdete,
    majd kiírjuk egytől n-ig a számokat(n+1 ig iterálunk)
    és a végén kiírjuk azt hogy: # ciklus vége
    """
    if debug:
        print("# ciklus kezdete:")
        for i in range(1,n+1):
            print(i, end=" ")
        print()
        print("# ciklus vége")
    else:
        for i in range(1,n+1):
            print(i, end=" ")
        print()


def main():
    loop(4)
    print()
    loop(8, debug=True)

if __name__ == "__main__":
    main()