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



'''BRUTE FORCE ALGO'''
# Python3 program for Naive Pattern
# Searching algorithm
def naiveSearch(pat, txt):
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
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)
            isItThere = True #Turn the control switch on
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
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print("Pattern found at index " + str(i))
                isItThere = True

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
    if not isItThere:
        print("-1")



'''Knuth-Morris-Pratt ALGO'''
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
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
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            isItThere = True
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    if not isItThere:
        print("-1")
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
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
        badChar[ord(string[i])] = i;
 
    # retun initialized list
    return badChar
 
def BoyerMooreSearch(pat, txt):
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
            j -= 1
 
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            isItThere = True
 
            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
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
    if not isItThere:
        print("-1")

# Driver Code
if __name__ == '__main__':
    txt = readFileToUpper("NoPatternsHere.txt")
    
    print("This is the Naive section\n")    
    for index in (readFile("WhatWeAreLookingFor.txt")):   
        print("\nWe are looking for: ", index)
        naiveSearch(index, txt)

    
    print("\n\nThis is the Rabin-Karp section\n")
    q = 101 #hash code prime number
    for index in (readFile("WhatWeAreLookingFor.txt")):        
        print("\nWe are looking for: ", index)
        rabinKarpSearch(index, txt, q)


    print("\n\nThis is the Knuth-Morris-Pratt section\n")
    for index in (readFile("WhatWeAreLookingFor.txt")):        
        print("\nWe are looking for: ", index)
        KMPSearch(index, txt)


    print("\n\nThis is the Boyer-Moore section\n")
    for index in (readFile("WhatWeAreLookingFor.txt")):        
        print("\nWe are looking for: ", index)
        BoyerMooreSearch(index, txt)


# A prime number


