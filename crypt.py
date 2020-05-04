# crypter

passwd = input('\nGive me a password to "encrypt" : ')
y = ''

for x in passwd:
    y = y + str(ord(x)) + '$'

print('\nYour password successful encrypted :D\n -->', y)
