#Import libraries
#
import os
import sys

#Setting directory path as command line argument
#
dir_path = sys.argv[1]

#Looping through every sub-directory within the parent directory
#
for root, dirs, files in os.walk(dir_path):
    for file in files:

        #Searching for all the files that end with .txt
        #
        if file.endswith('.txt'):

            #Displaying the program running through all the directories
            #
            print (root+'/'+str(file))

            #Finding files with .txt in their name
            #
fname = '*.txt'

#Trying to open the file if it ends with .txt
#
try:
    fhand = open(fname)
    counts = dict()

    #Counting the lines
    #
    for line in fhand:
        words = line.split()

        #Getting the words
  #
        for word in words:
            counts[word] = counts.get(word, 0) + 1

            #Printing the words
            #
    print(counts)
except:

    #Error message if file can not be opened
    #
    print('File cannot be opened:', fname)
