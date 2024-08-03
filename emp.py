import random

def check_attend():

    choice = random.randint(0, 1)
    return choice


def check_daily_wage(daily_hr, wage_per_hr):

    daily_wage = daily_hr * wage_per_hr
    print(f"Employee is present full time.")
    print(f"The daily wage is: {daily_wage}")


def main():

    daily_hr = 8
    wage_per_hr = 20
    choice=check_attend()
    if(choice==1):
        check_daily_wage(daily_hr, wage_per_hr)
    else:
        print("employee is absent")


if __name__=='__main__':
    main()

