import datetime
import random

n_iter = 100000
step_iter = 10000

# generate list of random dates
def generate_bday(n):
    if n<2 or n>100:
        raise "Error: given input must be in range [2,100]"
    start = datetime.datetime(2001,1,1)
    b_days = [start+datetime.timedelta(days=random.randint(0,364)) for i in range(n)]
    return b_days

# prints passed list of dates in specified format
def print_generated_bdays(b_day_list,format = "%d %b"):
    print("Generated birthdays are:")
    for b_day in b_day_list[:-1]:
        print(b_day.strftime(format),end=", ")
    print(b_day_list[-1].strftime(format),"\n")

# returns a pair of lists of birthdays with multiple repetitions
def find_repetitions(b_day_list):
    freq = []
    date = []
    for i in set(b_day_list):
        if b_day_list.count(i)>1:
            date.append(i)
            freq.append(b_day_list.count(i))
    return (date,freq)

# returns true if any date repeats else false
def is_repetition(b_day_list):
    return len(b_day_list) != len(set(b_day_list))

print("The birthday paradox by Aadeshveer Singh\n")
n = int(input("How many birthdays should I generate?(max100)\n> ")) # input number of birthdays
print("\n")

b_days = generate_bday(n)
print("Here is are the generated birthdays: \n")
print_generated_bdays(b_days)

x_date, x_freq = find_repetitions(b_days)
if(x_date!=[]):
    print(f"Following are some statistics: \nOut of {n} people-")
    for i in range(len(x_date)):
        print(f"{x_freq[i]} people have birthday {x_date[i].strftime("%d %b")}")
    print("")
else:
    print("It seems all of them have unique birthdays, but let us try some more number of times.\n")

print(f"Let us generate {n_iter} iterations:")
input("Press enter to continue")
count = 0
for i in range(n_iter):
    if i%step_iter == 0:
        print(f"{i} simulations run...")
    b_days = generate_bday(n)
    if(is_repetition(b_days)):
        count+=1
print(f"{n_iter} simulations run...\n")
print(f"On a simulatin of {n} birthdays {n_iter} times, there was a matching birthday in the group {count} times! This means that given {n} people there is a {count/n_iter*100:.2f}% chance that of having a matching birthday in that group.\nThat is probably more than you might have though.")
# TODO: write program to make multiple lists to estimate probability