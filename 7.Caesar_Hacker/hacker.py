def shifter(c,n):
    if 'A' <= c <= 'Z':
        return chr( ( ( ord(c) + n - ord('A') ) % 26 ) + ord('A') )
    elif 'a' <= c <= 'z':
        return chr( ( ( ord(c) + n - ord('a') ) % 26 ) + ord('a') )
    else:
        return c

print(" Caesar Cipher Hacker ".center(40,'*'))
inp = input("Enter the encrypted Caesar cipher message to hack.\n> ")
for i in range(26):
    print(f"\nKey {i}: ",end="")
    for j in inp:
        print(shifter(j,i),end="")