import random

foods = ['Pizza','Burger','Chhole Bhature','Dosa','Cake','Chocolate','Fried Chicken','Mango','Dragonfruit','Prawns','Alligator tails','Cockroach milk','protein shake','Chicken breast']
countries = ['India','Russia','Soviet Union','China','USA','Finland','Burundi','Mexico','Congo republic','Pakistan','Afghanistan','Bangladesh','Uganda','Nigeria','North Korea','Mongolia']
adjective = ['Republican','Democrat','Indian','Afghan','Communist','Chinese','Capitalist','Mafia','Russian','Soviet','American','Finnish','Burundian','Mexican','Congo','Pakistani','Bangladeshi','Ugandan','Negerian','North Korean','Mongolian']
adjective2 = ['big','small','huge','tiny','large','humongous']
individuals = ['Elon Musk','Warren Buffet','Mukesh Ambani','Gautam Adani','Arnold Schwarzenegger','Kim Kardashian','Tom Cruise','Leonardo DiCaprio','Diljit Dosanjh', 'Taylor Swift', 'Vladmir Putin', 'Kim Jong Un', 'Narendra Modi', 'Trump', 'Zelensky']
dead_individuals = ['Adolf Hitler','Joseph Stalin','Mahatma Gandhi','John F Kennedy','Winston Churchill','Albert Einstein','Lenin','Karl Marx','Franklin Roosevelt','Queen Elizabeth','Neil Armstrong']
stuff = ['food','music','cars','tanks','fans','houses','government','drinks','nuclear power','underwear','quantum mechanics','real estate']
times = ['early morning','during breakfast','at noon','in evening','before sleep','before going to toilet','after going to toilet','before running','before exercise','after running','after exercise']
companies = ['Google','Open AI','Meta','Amazon','Microsoft','Tata','Samsung','Apple','Nvidia']
organs = ['Leg','Eye','Blood','Terminal','Skin','Lungs','Breast','Pancreatic','Kidney','Bladder','Thyroid']
nutrients = ['nutrients','vitamin A','vitamin B','vitamin C','vitamin D','vitamin E','vitamin K','Proteins','Fibers','Carbohydrates','Healthy Fats']


def ten_big_inv():
    return f"{random.randint(3,10)} best investment opportunities in {random.choice(adjective)} {random.choice(stuff)} Industry!"

def spy():
    if(random.randbytes(1)):
        return f"Is {random.choice(individuals)} a {random.choice(adjective)} spy? Get the answers here!!!"
    return f"Was {random.choice(dead_individuals)} a {random.choice(adjective)} spy? Get the answers here!!!"

def fav_food():
    return f"Did You Know: {random.choice(individuals)}'s favourite food is {random.choice(foods)}? Click to know why!!"

def ambassador():
    return f"{random.choice(countries)} is paying ${random.randint(1,200)} million to {random.choice(individuals)}, to promote their {random.choice(stuff)} industry!!"

def assassin():
    return f"{random.choice(dead_individuals)}'s role in assassination of {random.choice(dead_individuals)}! It might be more than you think!!"

def bad_sci():
    return f"{random.randint(3,10)} Reasons why eating a {random.choice(adjective2)} {random.choice(foods)} {random.choice(times)} increase your lifetime by {random.randint(1,10)} years!!"

def think():
    return f"Control your mind: How not to think about {random.choice(stuff)} {random.choice(times)}"

def food_fut():
    return f"Future of {random.choice(adjective)} {random.choice(foods)} restraunts is bright. Says {random.choice(individuals)}"

def trip_to():
    return f"A trip to {random.choice(countries)} might be cheaper than you think!!"

def stock_inv():
    return f"You need to know! Which {random.randint(3,10)} stocks is {random.choice(individuals)} secretly investing in"

def big_tech():
    return f"{random.choice(companies)} is planning to spend {random.choice(adjective2)} money in {random.choice(stuff)} technology! Click to know deltails..."

def cause_cancer():
    return f"Did you know: Eating {random.choice(adjective2)} {random.choice(foods)}, {random.choice(times)} can cause {random.choice(organs)} cancer."

def suffering_cancer():
    return f"{random.choice(individuals)} is suffering from {random.choice(organs)} cancer. Here is proof!!"

def super_food():
    return f"{random.choice(foods)} is the future Super food with {random.choice(adjective2)} amount of {random.choice(nutrients)}!!"

print(" Clickbait Headline Generator ".center(50,'*'))

print("Want your website to trick people to look into ads?")
while(True):
    try:
        inp = input("Enter number of claickbait headlines to generate:\n> ")
        inp = int(inp)
        if(inp<=0):
            raise ValueError
        break
    except (ValueError,TypeError):
        print("Please enter a valid number.")

for _ in range(inp):
    x = random.randint(0,16)
    if(x==0):
        print(ten_big_inv())
    if(x==1):
        print(spy())
    if(x==2):
        print(fav_food())
    if x in [3,4]:
        print(bad_sci())
    if(x==5):
        print(assassin())
    if(x==6):
        print(think())
    if(x==7):
        print(food_fut())
    if(x==8):
        print(trip_to())
    if x in [9,10]:
        print(ambassador())
    if(x==11):
        print(big_tech())
    if(x==12):
        print(stock_inv())
    if x in [13,14]:
        print(cause_cancer())
    if(x==15):
        print(suffering_cancer())
    if(x==16):
        print(super_food())