def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name_list = fullname.split()
    init = ""
    for a_name in name_list:
        init = init + a_name[0]
        init = init.upper()
    return init
def main():
    fullname = input("What is your name?")
    print(get_initials(fullname))
    
if __name__ == "__main__":
    main()