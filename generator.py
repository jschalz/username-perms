#!/usr/bin/python3

import sys, getopt
from itertools import permutations

def getArgList(argv):
    elements = []
    special = False
    
    try:
        opts, args = getopt.getopt(argv,"hi:s:",["input=","special="])
    
    except getopt.GetoptError:
        print("generator.py -s <True or False> -i <input array>")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print("generator.py -i <input array>")
            sys.exit()
        
        elif opt in ("-i", "--input"):
            elements = arg.split(',')
        
        elif opt in ("-s", "--special"):
            if arg == "True":
                special = True
    
    if special:
        specialSet = "._-"
        for x in specialSet:
            elements += x

    return elements

def createPerms(elementArray):    
    perms = [''.join(x) for x in permutations(elementArray)]
    return perms

def main():
    args = sys.argv[1:]
    elements = getArgList(args)
    perms = createPerms(elements)
    for perm in perms:
        print(perm)

if __name__ == "__main__":
    main()
