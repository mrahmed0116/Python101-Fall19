import os
import argparse
import subprocess
import glob
import sys

try:
    import pathlib

except ImportError:
    if os.name == 'nt':
        subprocess.call(['python', '-m', 'pip', 'install', 'pathlib'])
        import pathlib
    else: # linux
        subprocess.call(['pip', 'install', 'pathlib'])
        import pathlib
        
if sys.version_info.major == 2:
    inputter = raw_input
else: # if python 3
    inputter = input

class AirportFilter(object):
    """
    :brief Class contains methods for obtaining input/output files and handles parsing logic.
    :param object   - class inherits object class.
    """
    def __init__(self, datFile, outFile, iata):
        """
        :brief Function initializes AirportFilter class and obtains input values from command line (if any).
        :param datFile  - input file (in .dat format).
        :param outFile  - output file to write filter results.
        :param iata     - user input for desired airport to be filtered.
        :return None
        """
        self.datFile = datFile
        self.outputFile = outFile
        self.airport = iata
        self.inputLines = []
        self.flightsDict = dict() # or self.flightsDict = {}
        
    def validateInputFile(self):
        """
        :brief Function prompts user for input file path and validates that input criteria has been met.
        :param -
        :return True on success, False on failure
        """
    
        if self.datFile == None or not os.path.isfile(self.datFile) or pathlib.Path(self.datFile).suffix.upper() != ".DAT":
            
            print("\nInput Dat file not provided. Providing 3 tries for correct input file entrance.\n")
            usr_trial = 3
        
            while usr_trial:
                usr_input = inputter("Trial %d, Input a correct file/format : " % usr_trial)
                try:
                    if os.path.isfile(usr_input) or pathlib.Path(self.datFile).suffix != "dat":
                        self.datFile = usr_input
                        break
                    else:
                        usr_trial = usr_trial - 1
                except TypeError:
                    usr_trial = usr_trial - 1
            
            try:
                if not os.path.isfile(self.datFile) or pathlib.Path(self.datFile).suffix != ".dat":
                    print("Failed to provide a valid input file. Terminating program.")
                    return False
            except TypeError:
                print("Failed to provide a valid input file. Terminating program.")
                return False

        print("\nInput file %s is verified.\n" % self.datFile)

        return True
            
    def validateOutputFile(self):
        """
        :brief Function checks for output file being provided, if not, will prompt user.
        :param -
        :return True on success, False on failure
        """

        if self.outputFile == None:
            self.outputFile = inputter("Please provide an output file: ")

            if self.outputFile == "":
                print("User hit Enter without input. Terminating program.")
                return False

        # os.path.isfile(self.outputFile) is the quickest way to get to the answer!

        dirpath = os.path.dirname(os.path.abspath(self.outputFile)) # get the parent directory
        outputFileExt = pathlib.Path(self.outputFile).suffix        # get the file extension of the output file
        files = glob.glob(os.path.join(dirpath, "*"+outputFileExt)) # get all files with matching extensions in parent dir

        if len(files) > 0:  # Files with similar extension exist
            for file in files:
                if self.outputFile in file:
                    usr_input = inputter(
                        "\nThe file %s already exists. Do you wish to overwrite existing file. Yes or No? " % self.outputFile)

                    if usr_input.upper() not in ["YES", "YA", "YEP", "YESSIR", "YOU ALREADY KNOW", "YEAH"]:
                        print("\nTerminating program as per instructions. Tip for next time, let the file be overwritten...\n")
                        return False

        return True

    def readInput(self):
        """
        :brief Funciton reads input dat file and stores logs in a dictionary.
        :param -
        :return None
        """
        print("\nGreat! Reading and processing data.")
        with open(self.datFile, "r") as dat:
            self.inputLines = dat.readlines()

        for line in self.inputLines:
            iata = line.split(",")[2]
            if iata in self.flightsDict.keys():
                self.flightsDict[iata].append(line)
            else:
                self.flightsDict[iata] = [line]
        return

    def processIATA(self):
        """
        :brief Function takes user input for IATA and writes flight logs to outputFile.
        :param -
        :return None
        """
        if self.airport == None:
            self.airport = inputter("\nEnter airport symbol: ")

        if self.airport.upper() in self.flightsDict.keys():
            print("\nFlight logs are written to %s.\n" % os.path.abspath(self.outputFile))
            with open(self.outputFile, "w+") as out:
                out.write("Logging flights initiated from airport %s\n" % self.airport)
                for logs in self.flightsDict[self.airport.upper()]:
                    out.write(logs)
        else:
            print("\nThe entry %s was not a valid IATA. Terminating program.\n" % self.airport.upper())

        print("Good bye!\n")
        return
        

if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(prog='Python101_Final_Proj')
    
    parser.add_argument('-I','--Input', action='store', type=str, help='Input file')
    parser.add_argument('-O', '--Output', action='store', type=str, help='Output file')
    parser.add_argument('-A', '--IATA', action='store', type=str, help='IATA characters')
    
    option = parser.parse_args()
    
    iataFilter = AirportFilter(datFile=option.Input, outFile=option.Output, iata=option.IATA)
    
    if iataFilter.validateInputFile():
        if iataFilter.validateOutputFile():
            iataFilter.readInput()
            iataFilter.processIATA()
        
    exit()
    
