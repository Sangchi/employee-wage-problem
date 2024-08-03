import random

def check_attend():

    choice = random.randint(0, 2)
    return choice

def check_daily_wage(daily_hr, wage_per_hr):

    daily_wage = daily_hr * wage_per_hr
    print(f"Employee is present full time.")
    print(f"The daily wage is: {daily_wage}")


def check_daily_half_wage(partime_hr, wage_per_hr):

    daily_half_wage = partime_hr * wage_per_hr
    print(f"Employee is present half time.") 
    print(f" half Daily wage is: {daily_half_wage}")

def main():

    daily_hr = 8
    partime_hr = 4
    wage_per_hr = 20
    choice=check_attend()

    match choice:
        case 0:
            result = 'Employee is absent'

        case 1:
            result = check_daily_wage(daily_hr, wage_per_hr)
            return result

        case 2:
            result = check_daily_half_wage(partime_hr, wage_per_hr)
            return result
        case _:
            result = "Choice is invalid"

    print(result)


if __name__ == '__main__':
    main()

