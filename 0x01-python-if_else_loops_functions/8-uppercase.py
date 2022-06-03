#!/usr/bin/python3
def uppercase(str):
    for i in str:
        strUpper = 0
        if ord(i) > 96 and ord(i) < 123:
            strUpper += ord(i)-32
        else:
            strUpper += ord(i)
        print("{:c}".format(strUpper), end="")
    print("")
