# -*- coding: utf-8 -*-
"""
￼
AUTHOR Harmanprit Tatla
VERSION 2015 - April - 9

PURPOSE: To plot the distribution of word frequencies in a book.
"""
#imports
import time
import numpy as np
import matplotlib.pyplot as plt
from sys import path, stdout
from os import chdir

# Global constants (as part of CompareBooks program)
NUM_WORDS_TO_PRINT = 20

#The following functions have been obtained from the CompareBooks.py program at
#http://www.cs.umanitoba.ca/~comp1012/CompareBooks.py; The functions that have
#been modified are indicated as such.
#********************BEGIN OF COPIED CODE**************************************

#************************MODIFIED***************************************** main
def main() :
    """Compiles a word frequency list for one book and plots word frequencies
    of words that are 4 characters or longer."""
    book1, wordDict1 = readBook() # Analyze  book
    plotDict(wordDict1, 50, book1) # Plot top 50 word frequencies
    theEnd() # Termination output

#************************MODIFIED*********************************** countWords
def countWords(words) :
    """Analyze a list of words, and return a dictionary of unique 4 character  
    or longer words, sorted, and the corresponding word frequencies"""
    
    # find and count the unique words (no duplicates)
    wordDict = {}
    for word in words :
        if len(word) >= 4 : # only consider words 4 characters or longer
            if word in wordDict : #if word in dict add 1 to its value
                wordDict[word] += 1
            else : #else word not in dict; add word to dict, set its value to 1
                wordDict[word] = 1
                
    # convert counts to frequencies
    total = float(sum(wordDict.values()))
    for word in wordDict :
        wordDict[word] /=  total # change from count to frequency
    return wordDict

#*******************************************************************getBookText
def getBookText(filename) :
    """Open a local book with the given name, read the contents, and return
    as a text string."""
    flink = open(filename, "rU")
    text = ""
    for eachline in flink :  # or just flink.readlines()
        text += eachline
    flink.close()
    fragment = text[:300] # excerpt to print

    # end excerpt at the end of a line
    pos = len(fragment) - 1
    while pos >= 0 and fragment[pos] != "\n" :
        pos -= 1

    fragment = "-- " + fragment[: pos + 1].replace('\n', '\n-- ') + "..."
    print "\nStart of %s:" % filename
    print fragment
    pause()
    return text

#************************************************************************ pause
def pause() :
    """Stop to let the user read recent output. Continue when they press
    Enter."""
    #print "\nPress Enter to continue ..."
    tmp = raw_input("Press Enter to continue ...\n")
    return

#**********************MODIFIED*************************************** plotDict
def plotDict(wordDict, numRows, bookName) :
    """Plot the top numRows frequencies; wordDict is a dict with word as key, 
    and values frequency of word. bookName is a character string of the name
    of a book."""

    freqList = wordDict.values() #List of frequencies of each word in wordDict
    freqList.sort(reverse=True)  #Sort frequencies of words largest to smallest 
    
    #Histogram plot of the top numRows frequencies 
    fig = plt.figure()
    fig.add_subplot(121)
    plt.hist(range(1, numRows + 1), bins = numRows, 
             weights = freqList[:numRows])
    plt.title("Distribution of word frequencies")
    plt.xlabel("Word ranking")
    plt.ylabel("Word frequency")
    
    #loglog plot of the top numRows frequencies
    fig.add_subplot(122)
    plt.loglog(range(1, 5 * numRows + 1), freqList[:5 * numRows], 
               label = bookName)
    plt.xlabel("Word ranking")
    plt.ylabel("Word frequency")
    plt.title("Word frequency vs Word ranking")
    plt.legend(loc = 'upper right')
    
    plt.show()
    
#************************MODIFIED*********************************** printWords
def printWords(wordFrequencies, numRows) :
    """Prints a table of the top numRows frequencies and corresponding words in
    wordFrequencies, which is a list of tuples in the form (freq, word)."""
    
    wordFrequencies.sort()
    print "\nWords        Frequencies"
    for freq, word in reversed(wordFrequencies[-numRows:]) :
        print "%-10s  %10.5f" % (word, freq)
    #prints sum of frequencies of all words in wordFrequencies, [0] to get 
    #frequency.
    print 'Sum of frequencies: %g' % sum([freq[0] for freq in wordFrequencies])
    
#***********************MODIFIED************************************** readBook
def readBook() :
    """Ask the user for a filename, read the contents, separate it into words,
    find unique words and count them, and return a list of sorted words and
    associated frequencies."""
    chdir(path[0])                #...........................find the folder
    print "\nEnter the name of a file to read:"
    filename = raw_input()
    text = getBookText(filename)   # one long string
    text = simplifyText(text)      # upper case; no punctuation
    words = text.split()           # list of words
    # Remove leading and trailing apostrophes; keep apostrophes inside
    words = [word.strip(" '") for word in words]
    wordDict = countWords(words) # wordDict[word] gives frequency
    wordFrequencies = [(freq, word) for word, freq in wordDict.items()]
    
    print "Most Frequent %d Words in %s with no less than 4 Words" % (
           NUM_WORDS_TO_PRINT,filename)
    printWords(wordFrequencies, NUM_WORDS_TO_PRINT)
    
    return filename, wordDict

#***************************************************************** simplifyChar
def simplifyChar(char) :
    "Convert non-alphanumerics except ' to blank"
    possibles = ' ' + char
    return possibles['A' <= char <= 'Z' or '0' <= char <= '9' or char == "'"]

#***************************************************************** simplifyText
def simplifyText(text) :
    """Convert all letters to uppercase, and all characters but letters and
    numbers and apostrophes to blanks and return the modified text."""
    charList = list(text.upper())
    charList = [simplifyChar(ch) for ch in charList]
    text = "".join(charList)
    return text

#******************END OF COPIED CODE******************************************

def theEnd():
    """Prints termination message to indicate succesful completion of 
       program."""
    print '\nProgrammed by Harmanprit Tatla'
    print 'Date:', time.ctime()
    print 'End of processing...' 
    return   

main() #call to start compare words program




