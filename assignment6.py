"""
I am sure you are all used to the drill by now,
just submit your assignment6.py to autolab. Make
sure that you include the main function and any
tests that you ran.

Rubric:
20 points backupFile()
10 points addSemester()
20 points reverseLine()
20 points storeTabDelimitedFile()
10 points main() and tests
20 points style and comments 
"""


def backupFile(inputFile, outputFile):
    """_Implement this method_
    Write a function that makes a backup of a file.
    Input is a path to some filename and the output filename.
    Save the input file to another file with the output name
    and the extension '.bak'
    """
    
    with open(inputFile, 'r') as f: # opening the classes.txt file or python file
        x = f.read()
        
    with open(outputFile, 'w') as f: # creating a classes.bak file within the folder containing this program
        f.write(x)



def addSemester(inputFile, outputFile):
    """_Implement this method_
    Write a function that takes as input an input file and and output file name.
    Read the input file and write to the output file the courses listed with 
    the semester that they occur in. For example 
    'cs 121' in the input file would be 'cs 121 fall' in the output file.
    You can find the courses and their semesters at http://schedules.wsu.edu
    Each class must be on its own line. Input classes are in classes.txt
    """

    
    fall_classes = ['cs 121', 'cs 223', 'cs 260', 'cs 215']
    spring_classes = ['cs 122', 'cs 166', 'cs 224', 'cs 251', 'cs 261']
    

    with open(inputFile, 'r') as f:
        newlist = f.readlines()  
        for i in range(len(newlist)):
            newlist[i] = newlist[i].strip()
        print(newlist)
        for i in newlist:
            print(i)                
        print("-----------------------")    # this is all taking each line in the text and converting it into a list while also getting rid of any new lines to make it easier to concatanate fall or spring

    with open(outputFile, 'w') as f:
        index = 0                       # this is a counter that is incrementing once every loop and is being used to index into the list 
        for i in newlist:   
            if i in fall_classes:   
                newlist[index] += " fall\n"
                index += 1
            elif i in spring_classes:
                newlist[index] += " spring\n"
                index += 1

                     
        original = ''.join(newlist)     # this brings together the finalized list into the original format just with the corresponding fall or spring
        print(original)
        f.write(original)

    

def reverseLine(inputFile, outputFile):
    """_Implement this method_
    Write a function that takes as input an input file and and output file name.
    Read the input file and output to the output file each line but reversed.
    You may NOT use any sorting algortihm. Do not reverse each character, for
    example if a line is "hello world" then it would be written as "world hello"
    """
    with open(inputFile, 'r') as f:             # opening the classes.txt file
        newlist = f.readlines()                 # creating a list containing each line from the classes file
        for i in range(len(newlist)):           
            newlist[i] = newlist[i].strip()     # getting rid of the newlines as to not interfere with the text reversal

    with open(outputFile, 'w') as f:
        reversedList = []

        for i in range(len(newlist)):           
            x = newlist[i].split()              # this will break up each elements string on their spaces to make it easier to reverse them
            x.reverse()
            original = ' '.join(x)              # this will bring it all back together in input files original text format
            reversedList.append(original + '\n')

        final = ''.join(reversedList)
        print(final)
        f.write(final)


        

def storeTabDelimitedFile(inputFile):
    """_Implement this method_
    Write a function that takes as input an input file and stores the contents in 
    a matrix. Each row in the matrix should be a line in the input file. Each element
    in a row should be an element from the line, delimited by a tab.
    """


    list0 = []
    with open(inputFile, 'r') as f:
        newlist = f.readlines()
        #print(newlist)
        for i in range(len(newlist)):
            #newlist[i] = newlist[i].strip('\t')
            newlist[i] = newlist[i].strip('\n') # this makes the matrix easier to read as i will not be converting back to original format
            x = newlist[i].split('\t')          # everytime a tab appears in a lines string, the string is split and is storing data in a list
            list0.append(x)
        print(list0)            # list0 is the matrix as it contains sublists and elements that can be individually accessed
             



def main():
    backupFile('classes.txt', 'out.bak')
    #backupFile('assignment6.py', 'assignment6.bak')
    #reverseLine('classes.txt', 'out2.txt')
    reverseLine('reversetest.txt', 'out2.txt')
    #addSemester('classes.txt', 'add_sem.txt')
    #storeTabDelimitedFile('classes.txt')

    #Put your tests here!!!
    #Remember to test as you go!!!


if __name__ == '__main__':
    main()
