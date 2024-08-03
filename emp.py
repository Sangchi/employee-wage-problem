import random

def check_attend():

    choice = random.randint(0, 1)
    return choice

def main():

    choice=check_attend()
    if(choice==1):
        print("employee is present ")

    else:
        print("employee is absent")


if __name__=='__main__':
    main()

