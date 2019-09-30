# Python 101 Series: Week 5

**Project Writeup:** 


**Flight Data Filter:**
 
A *filter* is a program that reads each record of an input file and creates a new output file containing only those records that match some qualifying criteria. For this assignment, you will construct a short Python filter program that will process real-world airline flight-routing data and produce a file containing only those records that represent flights arriving to and/or departing from a particular airport. 


Use your web browser to view the following URL: 

http://openflights.org/data.html 


This is a website that maintains information on airline flights. Browse the site, locate the section entitled: "*Route Database*" and download the routes.dat file (~2MB). This file describes all worldwide airline flight segments between various airports. You should also review the text that describes the content and format of the file. 


Write a Python program that will process this file and produce a smaller file containing only those flights that arrive at, or depart from, a designated airport. Your program should solicit the name of the input file, the name of the (filtered) output file and the IATA letter code for the selected airport. For example, Minneapolis is MSP and San Francisco is SFO, etc. 


**Requirements:**

Your program must do the following: 
- Solicit the name of the input route-data file from the user. If the file does not exist or fails to open, continue to solicit the file name a maximum of 3 times and then terminate the program 
- Solicit the name of the output (filtered) route-data file from the user. If the file exists, then ask the user if he/she would like to overwrite the existing file. If not, then terminate the program. 
- Solicit an IATA airport code from the user (e.g., MSP, SFO, etc.). Your program should accommodate entry in either upper or lower case. 
- Process the input file and produce an output file consisting only of the records of those flights that arrive and/or depart from the indicated airport. 


**Constraints:** 
- Do not import/use the Python csv or shutil modules. All other standard Python modules are acceptable, including os 
- All files must be properly opened and closed. 


**Example:** 


    Airport Routing Filter 
    Enter the source file name: routes.dat 
    Enter the output file name: mspdata 
    Enter airport symbol: msp Finished
    >>> ================================ RESTART 
    >>> 
    Airport routing filter 
    Enter the source file name: mickeymouse 
    File not found. Reenter: routes.dat 
    Enter the output file name: mspdata 
    File exists... overwrite? (y/n): y 
    Enter airport symbol: msp 
    Finished 
