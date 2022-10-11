#!/usr/bin/env python3
# encoding: utf-8

def main():
    print("1F")
    jarmuvek=['auto','villamos','metro']
    result=[s.upper() for s in jarmuvek]
    print(result)

    print("2F")
    names=['aladar','bela','cecil']
    result = [s.capitalize() for s in names]
    print(result)

    print("3F")
    result=[0 for i in range(0,11)]
    print(result)

    print("4F")
    result=[2*i for i in range(1,11)]
    print(result)

    print("5F")
    strings=['1','2','3','4','5','6','7','8','9','10']
    result=[int(s) for s in strings]
    print(result)

    print("6F")
    word="1234567"
    result=[int(s) for s in word]
    print(result)

    print("7F")
    sentence='The quick brown fox jumps over the lazy dog'.split()
    result=[len(w) for w in sentence]
    print(result)

    print("8F")
    sentence="python is an awesome language".split()
    result=[w[0] for w in sentence]
    print(result)

    print("9F")
    sentence='The quick brown fox jumps over the lazy dog'.split()
    result=[(w, len(w)) for w in sentence]
    print(result)

    print("10F")
    result=[i for i in range(10) if i%2==0]
    print(result)

    print("11F")
    result=[i*i for i in range(20) if i%2==0]
    print(result)

    print("12F")
    result=[i*i for i in range(20) if str(i*i)[-1]=="4"]
    print(result)

    print("13F")
    letters=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    result=""
    for c in letters:
        result+=c
    print(result)

    print("14F")
    fruit=['   apple   ','  banana   ','   kiwi   ']
    result=[w.strip() for w in fruit]
    print(result)

    print("15F")
    nums=[1,0,1,1,0,1,0,0]
    result=""
    for i in nums:
        result+=str(i)
    print(result)


if __name__ == "__main__":
    main()