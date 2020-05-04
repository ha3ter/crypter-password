# Decripter
passwd = input('\nGime the Hash to "Decrypt" : ')
y = ''

password = passwd.split('$')
password.remove('')

for x in password:
    y = y + (chr(int(x)))

print ('\nYour Hash successful Decrypted :D\n -->', y)
