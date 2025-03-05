import datetime
import random

n_iter = 100000
step_iter = 10000

# generate list of random dates
def generate_bday(n):
    start = datetime.datetime(2001,1,1)
    b_days = [start+datetime.timedelta(days=random.randint(0,364)) for i in range(n)]
    return b_days

# prints passed list of dates in specified format
def print_generated_bdays(b_day_list,format = "%d %b"):
    print("Generated birthdays are:")
    for b_day in b_day_list:
        print(b_day.strftime(format))

def find_repetitions(b_day_list):
    freq = []
    date = []
    for i in set(b_day_list):
        if b_day_list.count(i)>1:
            date.append(i)
            freq.append(b_day_list.count(i))
    return (date,freq)


print("The birthday paradox by Aadeshveer Singh")
n = int(input("How many birthdays should I generate?\n>")) # input number of birthdays
print("\n")
b_days = generate_bday(n)
print("Here is are the generated birthdays: ")
print_generated_bdays(b_days) # prints list of random dates
x_date, x_freq = find_repetitions(b_days)
if(x_date!=[]):
    print(f"Following are some statistics: \nOut of {n} people-")
    for i in range(len(x_date)):
        print(f"{x_freq[i]} people have birthday {x_date[i]}")
else:
    print("It seems all of them have unique birthdays, but let us try some more number of times")

print(f"Let us run {n_iter} iterations:")
# TODO: write program to make multiple lists to estimate probability