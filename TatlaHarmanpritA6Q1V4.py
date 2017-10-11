# -*- coding: utf-8 -*-
"""TatlaHarmanpritA6Q1
￼￼

COMP 1012 SECTION A01
INSTRUCTOR Terrance H. Andres
ASSIGNMENT: A6 Question 1
AUTHOR Harmanprit Tatla
VERSION 2015 - April - 9

PURPOSE: To plot expansions of a fractal curve, and to plot the distribution
of word frequencies in a book.
"""
#imports
import time
import numpy as np
import matplotlib.pyplot as plt
from sys import path, stdout
from os import chdir

# Global constants (as part of CompareBooks program)
NUM_WORDS_TO_PRINT = 20

def peanoCurve(expansion):
    """Given a positive integer for expansion, the number of expansions to 
    perform on the Peano curve, displays a plot with the expansions."""

    print 'Plotting Peano curve. Please wait.' #prints out wait message.
    stdout.flush() 
    
    #Sequence of points for Peano curve after its first expansion.
    p_ = np.array([0+0j, 1+0j, 1+1j, 2+1j, 2+0j, 1+0j, 1-1j, 2-1j, 2+0j, 
                   3+0j]) / 3.
    zz = p_ #Holds sequence of points for Peano curve for each expansion
    
    plt.figure() 
   
    #subplot of first expansion of Peano curve 
    plt.subplot(1, expansion, 1) # 1 row, expansion columns, loc 1
    plt.plot(p_.real, p_.imag, 'k') # x-axis = real num, y-axis = imaginary num
    plt.title('Expanded Once', fontsize = 10)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    #To make space between curve and margins of subplot
    plt.xlim(-0.15, 1.15)
    plt.ylim(-0.6, 0.6)

    #Expands the Peano curve expansion times                         
    for num in range(expansion-1):
        #since num starts from 0, num+2 to get correct loc for subplot
        plt.subplot(1, expansion, num+2)
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.xlim(-0.15, 1.15)
        plt.ylim(-0.6, 0.6) 
        
        #For each expansion, replaces line segment between consecutive points 
        #z1 and z2 by a path;(zz)[1:] used to get z2, the point next to each z1
        for z1, z2 in zip(zz, (zz)[1:]):
            #plots curve expansion by computing partial path between each z1 
            #and z2 then plotting it.
            plt.plot((z1 + p_ * (z2 - z1)).real, (z1 + p_ * (z2 - z1)).imag)
            
            #Appends each partial path to zz to make path for current expansion
            zz = np.append(zz, z1 + p_ * (z2 - z1)) 
            
            if num == 0: #if num==0 then plot title for second expansion.
                plt.title('Expanded Twice', fontsize = 10)
            else: #else num!=0; plot title for (num+2) expansion 
                  #since num starts at 0, +2 to get correct num for plot title
                plt.title('Expanded %d Times' % (num+2), fontsize = 10)
            
    plt.show()

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

peanoCurve(4) # call to get 4 expansions of Peano curve 
main() #call to start compare words program




