import datetime
import random


def generate_bday(n):
    start = datetime.datetime(2001,1,1)
    b_days = [start+datetime.timedelta(days=random.randint(0,364)) for i in range(n)]
    return b_days

def print_generated_bdays(b_day_list):
    print("Generated birthdays are:")
    for b_day in b_day_list:
        print(b_day.strftime("%d %b"))

def find_repetitions(b_day_list):
    pass # TODO: implement function to check repetitions


print("The birthday paradox by Aadeshveer Singh")
n = int(input("How many birthdays should I generate?\n>")) # input number of birthdays
print("\n")
b_days = generate_bday(n)
print_generated_bdays(b_days)

# TODO: write program to make multiple lists to estimate probability