# CSCI 3330 - CRN 22104 - Fall 2021 - Dr. Hu
# Holden Davis, Jordan Maxwell, Tyler Walters
# Project 2 - Analyzing and verifying asymptotic time complexity of sorting algorithms

#Random for generating data, Time for timing sorts, Sys to overcome recursion limit
import random
import time
import sys

sizelist = [100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000,250000,500000,750000,1000000]

#New variant, each sort+case generates its own data and times itself, has no return values, prints to file itself
def bubblebest(listindex: int, outfile: str, csvfile: str):
    #generate data according to case
    #start timer
    #sort data
    #end timer
    #write to file
    print("help")
def bubbleaverage(listindex: int, outfile: str, csvfile: str):
    print("help")
def bubbleworst(listindex: int, outfile: str, csvfile: str):
    print("help")

def quickbest(listindex: int, outfile: str, csvfile: str):
    print("help")
def quickaverage(listindex: int, outfile: str, csvfile: str):
    print("help")
def quickworst(listindex: int, outfile: str, csvfile: str):
    print("help")

def mergebest(listindex: int, outfile: str, csvfile: str):
    print("help")
def mergeaverage(listindex: int, outfile: str, csvfile: str):
    print("help")
def mergeworst(listindex: int, outfile: str, csvfile: str):
    print("help")

def radixbest(listindex: int, outfile: str, csvfile: str):
    print("help")
def radixaverage(listindex: int, outfile: str, csvfile: str):
    print("help")
def radixworst(listindex: int, outfile: str, csvfile: str):
    print("help")

def test(rangelimit: int):
    print("\n<!---STARTING---!>\n")
    #Open files for writing, outfile for results, csvfile to be imported to excel for graphing
    csvfile = open("csvfile.csv", "w")
    outfile = open("outfile.txt", 'w')
    #Set recursion limit to largest C integer to permit larger datasets
    sys.setrecursionlimit(2147483647)
    outfile.write("BUBBLE SORT\n\n")
    for i in range(0,rangelimit):
        bubblebest(sizelist[i], outfile, csvfile)
        bubbleaverage(sizelist[i], outfile, csvfile)
        bubbleworst(sizelist[i], outfile, csvfile)
    outfile.write("\nQUICK SORT\n\n")
    for i in range(0,rangelimit):
        quickbest(sizelist[i], outfile, csvfile)
        quickaverage(sizelist[i], outfile, csvfile)
        quickworst(sizelist[i], outfile, csvfile)
    outfile.write("\nMERGE SORT\n\n")
    for i in range(0,rangelimit):
        mergebest(sizelist[i], outfile, csvfile)
        mergeaverage(sizelist[i], outfile, csvfile)
        mergeworst(sizelist[i], outfile, csvfile)
    outfile.write("\nRADIX SORT\n\n")
    for i in range(0,rangelimit):
        mergebest(sizelist[i], outfile, csvfile)
        mergeaverage(sizelist[i], outfile, csvfile)
        mergeworst(sizelist[i], outfile, csvfile)
    #Close files
    csvfile.close()
    outfile.close()
    print("<!---All testing complete! See outfile.txt for results!---!>")
    print("\n<!---STOPPING---!>\n")

#Conduct testing suite operations
def main():
    print("Press 1 to call sorts without modifying recursion limit (SAFE)")
    print("Press 2 to call sorts with modified recursion limit (UNSAFE)")
    print("Press 0 to exit")
    result = input("---> ")
    if result == "1":
        test(5)
    elif result == "2": 
        sys.setrecursionlimit(2147483647)
        test(10)
    elif result == "0": sys.exit()
    else: print("\n<!---Command Not Understood--->\n")
    main()

main()