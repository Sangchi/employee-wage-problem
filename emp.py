import random

class EmployeeWage:

    def __init__(self):

        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.absent_count = 0

    def check_attend(self):

        choice = random.randint(0, 3)
        return choice

    def check_daily_wage(self, daily_hr, wage_per_hr):

        daily_wage = daily_hr * wage_per_hr
        print(f"Employee is present full time.")
        print(f"The daily wage is: {daily_wage}")
        return daily_wage

    def check_daily_half_wage(self, partime_hr, wage_per_hr):
        daily_half_wage = partime_hr * wage_per_hr
        print(f"Employee is present half time.")
        print(f"Half Daily wage is: {daily_half_wage}")
        return daily_half_wage

    def check_monthly_wage(self):
        for _ in range(20):
            choice = self.check_attend()
            if choice == 1:
                self.daily_wage_count += 1
            elif choice == 2:
                self.half_daily_count += 1
            else:
                self.absent_count += 1

        daily_wage = 160
        half_daily_wage = 80
        total_monthly_wage = daily_wage * self.daily_wage_count + half_daily_wage * self.half_daily_count

        print(f"Employee is part-time present count={self.half_daily_count}")
        print(f"Employee is present full time count={self.daily_wage_count}")
        print(f"Employee absent count={self.absent_count}")
        print(f"Total monthly wage is={total_monthly_wage}")

    def check_for_hundred_hr_twenty_days(self):
        total_hr = 0
        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.absent_count = 0

        for _ in range(20):
            if total_hr <= 100:
                choice = self.check_attend()
                if choice == 1:
                    self.daily_wage_count += 1
                    total_hr += 8
                elif choice == 2:
                    self.half_daily_count += 1
                    total_hr += 4
                else:
                    self.absent_count += 1

        daily_wage = 160
        half_daily_wage = 80
        total_monthly_wage = daily_wage * self.daily_wage_count + half_daily_wage * self.half_daily_count

        print("The employee wage for 100 hr and 20 working days given below:")
        print(f"Employee is part-time present count={self.half_daily_count}")
        print(f"Employee is present full time count={self.daily_wage_count}")
        print(f"Employee absent count={self.absent_count}")
        print(f"Total hours are {total_hr}")
        print(f"Total monthly wage is={total_monthly_wage}")

def main():
    emp = EmployeeWage()
    daily_hr = 8
    partime_hr = 4
    wage_per_hr = 20

    choice = emp.check_attend()

    match choice:
        case 0:
            print('Employee is absent')
        case 1:
            emp.check_daily_wage(daily_hr, wage_per_hr)
        case 2:
            emp.check_daily_half_wage(partime_hr, wage_per_hr)
        case 3:
            emp.check_monthly_wage()
            emp.check_for_hundred_hr_twenty_days()
        case _:
            print("Choice is invalid")


if __name__ == "__main__":
    main()





