# dictionaries.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    '''
    - creation
    '''
    # create an empty dictionary named "dict" and print it

    dict = {}
    print(dict)
    print()

    # open your book to p. 401
    # create the "passwd" dictionary and print it

    passwd = {"guido":"superprogrammer","turing":"genius","bill":"monopoly"}
    print(passwd)
    print()

    '''
    - element access
    '''
    # using the square bracket notation print out the value for "turing"

    print(passwd["turing"])
    print()

    '''
    - element updates
    '''
    # using the square bracket notation update the value for "turing" 
    # to "super genius", then print the dictionary

    passwd["turing"] = "super genius"
    print(passwd)
    print()

    '''
    - element insertion
    '''
    # add a new key value pair to passwd
    # key = "new key"
    # value = "new key value"

    passwd["amp"]="boss"

    # print passwd

    print(passwd)
    print()

    '''
    - element deletion
    '''
    # delete "turing" from passwd and print passwd

    del passwd["turing"]
    print(passwd)
    print()

    '''
    - Value cannot be found after being deleted
    - Result printed quite literally
    - I think I started to mess up around here
    '''
    # print the result of get("turing")

    print("NameError: name 'get' is not defined")
    print()

    # Use the "in" keyword to search the dictionary
    # print the value returned by ' "turing" in passwd '

    "turing" in passwd
    print("TypeError: 'builtin_function_or_method' object is not subscriptable")

    '''
    - some dictionary methods
    '''
    # print the list of keys

    for key in passwd:
        print(key)
        print()

    # print the list of values

    for val in passwd:
        print(val)
        print()

    # print the list of items - key-value pairs

    for key,val in passwd():
        print(key,val)

    '''
    - deletion
    '''
    # delete all entries from passwd, then print it
    

main()