try:
    import pyperclip
except ModuleNotFoundError:
    print("You do not have the pyperclip module installed, The output will not be copied to clipboard.")

# shifts a character by given number (+ve for encryption and -ve for decryption)
def shifter(c,n):
    if 'A' <= c <= 'Z':
        return chr( ( ( ord(c) + n - ord('A') ) % 26 ) + ord('A') )
    else:
        return c


print(" Caesar Ciphar ".center(40,'*'))

# Taking input for encryption and decryption
while(True):
    inp = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
    if inp.lower() in ('e','d'):
        inp = inp.lower()
        break
    print("Invalid input! Please enter 'e' to encrypt and 'd' to decrypt.")

# Taking value of key as input
while(True):
    try:
        key = int(input("Please enter the key to use(0-25).\n> "))
        if key<0 or key>25:
            print("Key must lie between 0 and 25(both inclusive).")
        else:
            break
    except ValueError:
        print("Please Enter a valid numeric key.")

motive = 'encrypt' if inp == 'e' else 'decrypt'
message = input(f"Enter message to {motive}.\n> ")
output = "".join(shifter(i.upper(),key if inp == 'e' else -key) for i in message)
print(output)
try:
    pyperclip.copy(output)
    print(f"Full {motive}ed text copied to clip board.")
except Exception as e:
    print(f"Failed to copy output to clipboard: {e}\nYou may copy it manually.")
