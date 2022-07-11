#!/user/bin/env python3
"""Alta3 Research | RZFreeser
    print() - display data to std out"""

# below is a funtion containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")

    # display the input back to the user
    print("You told me the IPv4 is: " + user_input)
    
    # asking user for 'vendor name'
    vendor = input("Please input the vendor name: ")
    print(vendor)

# this calls main
main()

