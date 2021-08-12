#Analysis of Algorithms - CSCI 323
#Assignment 3
#Ben Kluger/Andrew Pak/Tania Chowdhury (GROUP)
#WEBSITES USED
'''
https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
'''

import numpy as np
import pandas as pd
import time
import matplotlib
import matplotlib.pyplot as plt
global naiveCount
naiveCount = 0
global rkCount
rkCount = 0
global kmpCount
kmpCount = 0
global bmCount
bmCount = 0
myTable = pd.DataFrame(columns=['Name of Algo', 'Pattern', 'Index Start', 'Avg run time (in ms)', 'Comparisons'])


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



'''BRUTE FORCE ALGO'''
# Python3 program for Naive Pattern
# Searching algorithm
def naiveSearch(pat, txt):
    global naiveCount
    global indexStarter
    indexStarter = []
    isItThere = False #Set the control switch to off
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
         
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                naiveCount += 1   
                ########################print("The index is:",i+j, ". The next character is:\'", txt[i+j], "\'")#######################        
                break
            naiveCount += 1
            j += 1
 
        if (j == M):
            #print("Pattern found at index ", i)
            isItThere = True #Turn the control switch on
            print("The index is:",i+j, ". The next character is: \'", txt[i+j], "\' We have found a match.")
            indexStarter.append(i)
        naiveCount += 1
    if not isItThere: #If the index is not there then we print a "-1"
        print("-1")
        


'''RABIN KARP ALGO'''
# RABIN KARP SECTION

# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number

def rabinKarpSearch(pat, txt, q):
    global rkCount
    global indexStarter
    indexStarter = []
    isItThere = False
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1


    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p==t:
            rkCount += 1
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    rkCount += 1
                    #####################print("The index is:",i+j, ". The next character is: \'", txt[i+j], "\' We have found a match.")####################
                    break
                else: 
                    j+=1
                    rkCount += 1


            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print("The index is:",i+j, ". The next character is: \'", txt[i+j], "\' We have found a match.")
                #print("Pattern found at index " + str(i))
                isItThere = True
                indexStarter.append(i)
            rkCount += 1

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
            rkCount += 1
        rkCount += 1
    if not isItThere:
        print("-1")



'''Knuth-Morris-Pratt ALGO'''
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    global kmpCount
    global indexStarter
    indexStarter = []
    isItThere = False
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        kmpCount += 1    
  
        if j == M:
            #print ("Found pattern at index " + str(i-j))
            print("The index is:",i-j+M, ". The next character is: \'", txt[i-j+M], "\' We have found a match.") #M == len(pat)
            indexStarter.append(i-j)
            isItThere = True
            j = lps[j-1]
            kmpCount += 1

  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
                kmpCount += 1
            else:
                i += 1
                kmpCount += 1
            kmpCount += 3
    if not isItThere:
        print("-1")
  
def computeLPSArray(pat, M, lps):
    global kmpCount
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            kmpCount += 1
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
            kmpCount += 2


'''Boyer-Moore Algo'''
# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm
 
NO_OF_CHARS = 256
 
def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''
 
    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS
 
    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i
 
    # retun initialized list
    return badChar
 
def BoyerMooreSearch(pat, txt):
    global bmCount
    global indexStarter
    indexStarter = []
    isItThere = False
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)
 
    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)
 
    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1
 
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            bmCount += 1
            j -= 1
 
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            #print("Pattern occur at shift = {}".format(s))
            print("The index is:",s+j+m+1, ". The next character is: \'", txt[s+j+m+1], "\' We have found a match.") #m == len(pat)
            isItThere = True
            indexStarter.append(format(s))
            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
            bmCount += 1
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])
        bmCount += 1
    if not isItThere:
        print("-1")



# Driver Code

nTrials = 1

if __name__ == '__main__':
    txt = readFileToUpper("input1.txt") 
    rowCounter = 0
    for x in range(0, nTrials):

        howLongItTakes = 0
        print("This is the Naive section\n")    
        for index in (readFile("WhatWeAreLookingFor.txt")):   
            print("\nWe are looking for: ", index)
            startTime = time.time()
            naiveSearch(index, txt)
            howLongItTakes += time.time() - startTime
            myTable.loc[rowCounter] = ['Naive', index, indexStarter, howLongItTakes*1000, naiveCount]
            rowCounter += 1
            
        
        #print("\n\n Average time for", nTrials, "trials of Naive Algorithm: ", howLongItTakes/nTrials *1000, "ms")
        #print("\n\n Comparisons for Naive's: ", naiveCount/nTrials)
        


        howLongItTakes = 0
        print("\n\nThis is the Rabin-Karp section\n")
        q = 101 #hash code prime number
        for index in (readFile("WhatWeAreLookingFor.txt")):        
            print("\nWe are looking for: ", index)
            startTime = time.time()
            rabinKarpSearch(index, txt, q)
            howLongItTakes += time.time() - startTime
            myTable.loc[rowCounter] = ['Rabin-Karp', index, indexStarter, howLongItTakes*1000, rkCount]
            rowCounter += 1
        #print("\n\n Average time for", nTrials, "trials of Rabin-Karp's Algorithm: ", howLongItTakes/nTrials *1000, "ms")
        #print("\n\n Comparisons for RK's: ", rkCount/nTrials)

        howLongItTakes = 0
        print("\n\nThis is the Knuth-Morris-Pratt section\n")
        
        for index in (readFile("WhatWeAreLookingFor.txt")):        
            print("\nWe are looking for: ", index)
            startTime = time.time()
            KMPSearch(index, txt)
            howLongItTakes += time.time() - startTime
            myTable.loc[rowCounter] = ['Knuth-Morris-Pratt',index, indexStarter,howLongItTakes*1000, kmpCount]
            rowCounter += 1
        #print("\n\n Average time for", nTrials, "trials of Knuth-Morris-Pratt Algorithm: ", howLongItTakes/nTrials *1000, "ms")
        #print("\n\n Comparisons for KMP's: ", kmpCount/nTrials)

        howLongItTakes = 0
        print("\n\nThis is the Boyer-Moore section\n")
        
        for index in (readFile("WhatWeAreLookingFor.txt")):        
            print("\nWe are looking for: ", index)
            startTime = time.time()
            BoyerMooreSearch(index, txt)
            howLongItTakes += time.time() - startTime
            myTable.loc[rowCounter] = ['Boyer-Moore', index, indexStarter, howLongItTakes*1000, bmCount]
            rowCounter += 1
        #print("\n\n Average time for", nTrials, "trials of Boyer-Moore Algorithm: ", howLongItTakes/nTrials *1000, "ms")
        #print("\n\n Comparisons for BM's: ", bmCount/nTrials)

        print (myTable)

    #MATPLOTLIB STUFF FOR FUN,run command "pip install -U matplotlib" if you dont have matplotlib

    ax = myTable.plot(kind='bar',x='Name of Algo', y='Comparisons',color='red')
    ax2 = ax.twinx()
    ax2.set_ylabel("Pattern", color="purple", fontsize=14)
    ax2.plot(myTable['Pattern'], color='purple')
    plt.savefig("myGraph1.png")
    
    #timePlot is for the time
    timePlot = myTable.plot(kind = 'scatter', x = 'Name of Algo', y = 'Avg run time (in ms)', color = 'blue')
    
    
    

    #Show the plot
    plt.show()
   