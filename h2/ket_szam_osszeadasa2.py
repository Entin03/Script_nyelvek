# main.py
import sys

def main():

    if len(sys.argv)!=3:
        print('Két számot adj meg!')
        return
    else:
        print(int(sys.argv[1])+int(sys.argv[2]))

if __name__ == "__main__":
    main()
