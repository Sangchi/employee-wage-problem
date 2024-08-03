import random

def check_attend():

    choice = random.randint(0, 3)
    return choice

def check_daily_wage(daily_hr, wage_per_hr):

    daily_wage = daily_hr * wage_per_hr
    print(f"Employee is present full time.")
    print(f"The daily wage is: {daily_wage}")

def check_daily_half_wage(partime_hr, wage_per_hr):

    daily_half_wage = partime_hr * wage_per_hr
    print(f"Employee is present half time.") 
    print(f" half Daily wage is: {daily_half_wage}")

def check_monthly_wage():

    daily_wage_count = 0
    half_daily_count = 0
    absent_count=0

    for i in range(20):
        choice = check_attend()
        if choice == 1:
            daily_wage_count += 1

        elif choice == 2:
            half_daily_count += 1

        else:
            absent_count +=1


    daily_wage = 160
    half_daily_wage = 80
    total_monthly_wage = daily_wage * daily_wage_count + half_daily_wage * half_daily_count
    print(f"employee is part time present count={half_daily_count}")
    print(f"emplyee is present full time count={daily_wage_count}")
    print(f"employee absent count={absent_count}")
    print(f"total_monthly_wage is={total_monthly_wage}")

def main():

    daily_hr = 8
    partime_hr = 4
    wage_per_hr = 20
    choice=check_attend()

    result = ""
    match choice:
        case 0:
            result = 'Employee is absent'

        case 1:
            result = check_daily_wage(daily_hr, wage_per_hr)
            return result

        case 2:
            result = check_daily_half_wage(partime_hr, wage_per_hr)
            return result

        case 3:
            result=check_monthly_wage()
            return result
        case _:
            result = "Choice is invalid"

    print(result)


if __name__ == '__main__':
    main()
