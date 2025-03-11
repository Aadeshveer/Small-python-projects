import datetime

CELL_WIDTH = 12
CELL_HEIGHT = 5
DAYS = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
MONTHS = ["january","february","march","april","may","june","july","august","september","october","november","december"]

print(" Calendar Maker ".center(40,'*'))

print()

while(True):
    year = input("Enter year for the calender\n> ")
    try:
        year = int(year)
        break
    except ValueError:
        print("Please enter a valid Year")

while True:
    month = input("Enter month for the calender(1 to 12)\n> ")
    try:
        month = int(month)
        if 0<month<=12:
            break
        else:
            print("Invalid month! Enter an integer between 1 and 12.")
    except ValueError:
        print("Please enter a valid month")

calendar = ''

calendar+=f"{MONTHS[month-1].capitalize()} {year}".center(7*CELL_WIDTH+8)+'\n'
for day in DAYS:
    calendar+='.'
    calendar+=day.capitalize().center(CELL_WIDTH,'.')
calendar+='.\n'
first_day = datetime.date(year=year,month=month,day = 1)
date = first_day - datetime.timedelta(first_day.weekday())
first = True
while(date.month==month or first):
    calendar+=('+'+'-'*CELL_WIDTH)*7+'+\n'
    for i in range(7):
        calendar+='|'+str(date.day).ljust(CELL_WIDTH)
        date+=datetime.timedelta(days=1)
    calendar+='|\n'
    for j in range(CELL_HEIGHT-1):
        for i in range(7):
            calendar+='|'.ljust(CELL_WIDTH+1)
        calendar+='|\n'
    first = False
calendar+=('+'+'-'*CELL_WIDTH)*7+'+'
print(calendar)

file_name = f"Calendar_{month}_{year}"
try:
    with open(file_name,'w') as file:
        file.write(calendar)
    print(f"Written to {file_name}")
except FileExistsError:
    print("File already exists")