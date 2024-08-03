import random

class EmployeeWage:
    def __init__(self):
        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.absent_count = 0
        self.total_hours = 0

    def check_attend():

        return random.randint(0, 3)

    def calculate_daily_wage(self, hours, wage_per_hour):

        return hours * wage_per_hour

    def check_daily_wage(self, daily_hours, wage_per_hour):

        daily_wage = self.calculate_daily_wage(daily_hours, wage_per_hour)
        return daily_wage

    def check_daily_half_wage(self, part_time_hours, wage_per_hour):

        daily_half_wage = self.calculate_daily_wage(part_time_hours, wage_per_hour)
        return daily_half_wage


    def check_for_hours(self, max_hours, daily_hours, part_time_hours, wage_per_hour, total_days):

        self.daily_wage_count = 0
        self.half_daily_count = 0
        self.absent_count = 0
        self.total_hours = 0

        for _ in range(total_days):
            if self.total_hours < max_hours:
                choice = EmployeeWage.check_attend()
                if choice == 1:
                    self.daily_wage_count += 1
                    self.total_hours += daily_hours
                elif choice == 2:
                    self.half_daily_count += 1
                    self.total_hours += part_time_hours
                else:
                    self.absent_count += 1

        total_monthly_wage = (self.calculate_daily_wage(daily_hours, wage_per_hour) * self.daily_wage_count +
                              self.check_daily_half_wage(part_time_hours, wage_per_hour) * self.half_daily_count)

        print("The employee wage for  hours and working days given below:")
        print(f"Employee is part-time present count={self.half_daily_count}")
        print(f"Employee is present full time count={self.daily_wage_count}")
        print(f"Employee absent count={self.absent_count}")
        print(f"Total hours are {self.total_hours}")
        print(f"Total monthly wage is={total_monthly_wage}")

def main():

    emp1 = EmployeeWage()
    daily_hours1 = 8
    part_time_hours1 = 4
    wage_per_hour1 = 20
    total_days1 = 20

    emp2 = EmployeeWage()
    daily_hours2 = 10
    part_time_hours2 = 5
    wage_per_hour2 = 25
    total_days2 = 22

    print("Company 1:")
    emp1.check_for_hours(100, daily_hours1, part_time_hours1, wage_per_hour1, total_days1)
    print("\nCompany 2:")
    emp2.check_for_hours(120, daily_hours2, part_time_hours2, wage_per_hour2, total_days2)


if __name__ == "__main__":
    main()


'''
output-
Company 1:
The employee wage for  hours and working days given below:
Employee is part-time present count=7
Employee is present full time count=3
Employee absent count=10
Total hours are 52
Total monthly wage is=1040

Company 2:
The employee wage for  hours and working days given below:
Employee is part-time present count=4
Employee is present full time count=7
Employee absent count=11
Total hours are 90
Total monthly wage is=2250
'''




