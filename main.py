import sys
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


from findFirstRepeatedN import findFirstRepeatedN
from pathChecker import pathChecker
from coinFlip import coinFlip

if __name__ == '__main__':
    # print_hi('PyCharm')
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [10, 12, 13, 4, 5, 7, 9]
    print(findFirstRepeatedN(list1, list2))

    if pathChecker(r"C:\Users\diabomba\Desktop"):
        print("OK")
    else:
        print("NOK")

    flips = [0,1,1,0]
    print(coinFlip(flips))