# Python 101 project
# Simple example solution

import os

def filter_routes():
    print('Airport Routing Filter')
    tries = 0
    valid_file = False
    while tries < 3 and not valid_file:
        fname = raw_input('Enter the source file name: ')
        if os.path.exists(fname):  # check if given input file exists
            ofile = open(fname, 'r')  # open file for reading
            output_file = raw_input('Enter the output_file file name: ')
            valid_file = True  # now while loop condition will fail
            if os.path.exists(output_file):  # check if there's already an output file with the same name
                ovwrite = raw_input('File exists... overwrite? (y/n): ')
                if ovwrite == 'y':  # else just exit program
                    newFile = open(output_file, 'w')
                    symb = raw_input('Enter airport symbol: ')
                    line = ofile.readline()  # get the first line in the file
                    while line != '':  # read until no more lines to be read
                        split_lines = line.split(',')  # returns line in a list without the commas
                        if symb.upper() in split_lines:  # check if symbol.upper() e.g. SMF is in the list split_lines
                            newFile.write(line)  # write the line to the output file
                        line = ofile.readline()  # get the next line in the file
                    ofile.close()
                    newFile.close()
            else:
                newFile = open(output_file, 'w')  # open the file for writing
                symb = raw_input('Enter airport symbol: ')
                line = ofile.readline()  # get the first line in the file
                while line != '':   # read until no more lines to be read
                    split_lines = line.split(',')   # returns line in a list without the commas
                    if symb.upper() in split_lines:  # check if symbol.upper() e.g. SMF is in the list split_lines
                        newFile.write(line)     # write the line to the output file
                    line = ofile.readline()  # get the next line in the file
                ofile.close()
                newFile.close()
            print('Finished')

        else:
            tries += 1
filter_routes()