#Analysis of Algorithms - CSCI 323
#Assignment 3
#Ben Kluger

def readFileToUpper(input):
    with open(input) as f:
        content = f.read().upper()
        f.close()
        #print(content)
        return content

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words
#print(readFile("WhatWeAreLookingFor.txt"))




#readFileToUpper('input2')



'''BRUTE FORCE METHOD'''
# Python3 program for Naive Pattern
# Searching algorithm
def search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)
            continue
 
# Driver Code
if __name__ == '__main__':
    txt = readFileToUpper("input1.txt")
    for index in (readFile("WhatWeAreLookingFor.txt")):
        print("\nWe are looking for: ", index)
        search(index, txt)
        
 
