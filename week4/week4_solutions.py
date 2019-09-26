# week 4 challenges solutions

# 1.) Write a Python program to convert month name to a number of days.
#
# Example:
#
#      - Input the name of Month: February
#      - No. of days: 28/29 days


def get_num_days():
    print("List of months: January, February, March, April, May, June, "
          "July, August, September, October, November, December")
    month_name = input("Input the name of Month: ")

    if month_name == "February":
        print("No. of days: 28/29 days")
    elif month_name in ("April", "June", "September", "November"):
        print("No. of days: 30 days")
    elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
        print("No. of days: 31 day")
    else:
        print("Wrong month name")
# get_num_days()


# 2.) Write a function that computes the net amount of a bank account based a transaction log from console input.

def get_balance():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D":
            netAmount += amount  # same as netAmount = netAmount + amount
        elif operation == "W":
            netAmount -= amount  # same as netAmount = netAmount - amount
        else:
            pass
    print(netAmount)
# get_balance()

# 3.) Write a Python program to read a text file line by line store it into an array. Print the array.

def read_file(fname):
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line)
        print(content_array)

read_file('sample_text.txt')
