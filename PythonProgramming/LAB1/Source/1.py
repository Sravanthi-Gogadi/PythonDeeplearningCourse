import re
# function definition
def check():
    while True:
        # Take the input from user
        password = input("Enter a password: ")
        # Check the length of the password
        if len(password)<6 or len(password)>16:
            print("Please make sure your password is at least 6 characters but not more than 16 characters")
        # Check whether a number is included or not
        elif re.search('[0-9]',password) is None:
            print("Please make sure your password has a number in it")
        # Check whether the password has a uppercase in it
        elif re.search('[A-Z]',password) is None:
            print("Please make sure your password has atleast one capital letter in it")
        # Check whether a password has lowercase in it
        elif re.search('[a-z]',password) is None:
            print("Please make sure that your password has atleast one lowercase letter")
        # Check whether password includes special characters
        elif re.search('[$@!*]',password) is None:
            print("Please make sure your password has special characters like $@!*")
        # If all are validated the user can login
        else:
            print("Thank you! You can now proceed")
            break
# function call
check()

