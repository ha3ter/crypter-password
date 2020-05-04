# Crypter password v2 ha3ter@gmail.com
print('''
  ____    __   __   _____ _____      
 / ___|_ _\ \ / / _|_   _|___ / _ __ 
| |   | '__\ V / '_ \| |   |_ \| '__|
| |___| |   | || |_) | |  ___) | |   
 \____|_|   |_|| .__/|_| |____/|_|   
               |_| Coded by ha3ter  

''')
def encrypt():

    passwd = input ('\nGive me the password to encrypt : ')
    f = ''

    my_dict = {'A': '0AD4', 'B': 'OEU3', 'C': 'CDK9', 'D': '0XA7', 'E': 'QHSD', 'F': 'DVJD', 'G': 'RTA3', 'H': 'QWE8',
               'I': 'SNAP', 'J': 'FLSI', 'K': '0A24', 'L': '1AE4', 'M': '0F99', 'N': 'MNI0', 'O': 'SEQ4', 'P': 'QWQW',
               'Q': 'WKZ3', 'R': '3Y#5', 'S': 'X^21', 'T': 'ZAA1', 'U': '!R3Y', 'V': 'Y$3Y', 'W': 'PIS0', 'X': 'ADJI',
               'Y': 'EFSF', 'Z': '0NGR', 'a': '6OKH', 'b': 'YUGF', 'c': 'Z13G', 'd': 'MRD3', 'e': 'ZE3T', 'f': 'HA3T',
               'g': 'PIYU', 'h': 'SGRT', 'i': 'CVI3', 'j': '0FDH', 'k': 'IA5K', 'l': '0H55', 'm': '3JFG', 'n': 'VI08',
               'o': 'AKVH', 'p': 'AOFR', 'q': '4ORL', 'r': 'DNV2', 's': 'ADS9', 't': 'VP0E', 'u': 'QGAR', 'v': 'KOR2',
               'w': 'KDB9', 'x': 'PWZV', 'y': 'V912', 'z': 'X5M8', '1': 'COW3', '2': 'DAQQ', '3': 'FUCK', '4': 'SOW1',
               '5': 'D36K', '6': 'RF2E', '7': 'RTTR', '8': 'PRHV', '9': 'W4TY', '0': '4G3F', '@': '24GB', '#': 'K9D3',
               '%': 'XNQ3', '^': 'AE2O', '&': '0RSA', '*': 'NSAX', '(': 'HA3R', ')': 'PANL', '_': 'FAN3', '+': 'SNAL',
               '-': 'CVK2', '=': '0F82', '/': '3BFV', '~': '34KK', '|': 'BASE', '\\': 'SAN4', '?': 'NLBU', '.': '0X3E',
               '$': '3HRJ', '"': 'IL93', ':': 'M7E2', ';': 'KV62', ',': 'LA23', "'": 'XMAP', '>': 'CP02', '<': 'V14Y',
               '!': 'IDV3'}

    for i in passwd:
        f = f + my_dict[i]
        
    print('\nYour password successful Encrypted :D\n --> ', f)

def decrypt():

    passwd = str(input ('\nGive me the Hash to decrypt : '))
    
    my_dict = {'0AD4': 'A', 'OEU3': 'B', 'CDK9': 'C', '0XA7': 'D', 'QHSD': 'E', 'DVJD': 'F', 'RTA3': 'G', 'QWE8': 'H',
               'SNAP': 'I', 'FLSI': 'J', '0A24': 'K', '1AE4': 'L', '0F99': 'M', 'MNI0': 'N', 'SEQ4': 'O', 'QWQW': 'P',
               'WKZ3': 'Q', '3Y#5': 'R', 'X^21': 'S', 'ZAA1': 'T', '!R3Y': 'U', 'Y$3Y': 'V', 'PIS0': 'W', 'ADJI': 'X',
               'EFSF': 'Y', '0NGR': 'Z', '6OKH': 'a', 'YUGF': 'b', 'Z13G': 'c', 'MRD3': 'd', 'ZE3T': 'e', 'HA3T': 'f',
               'PIYU': 'g', 'SGRT': 'h', 'CVI3': 'i', '0FDH': 'j', 'IA5K': 'k', '0H55': 'l', '3JFG': 'm', 'VI08': 'n',
               'AKVH': 'o', 'AOFR': 'p', '4ORL': 'q', 'DNV2': 'r', 'ADS9': 's', 'VP0E': 't', 'QGAR': 'u', 'KOR2': 'v',
               'KDB9': 'w', 'PWZV': 'x', 'V912': 'y', 'X5M8': 'z', 'COW3': '1', 'DAQQ': '2', 'FUCK': '3', 'SOW1': '4',
               'D36K': '5', 'RF2E': '6', 'RTTR': '7', 'PRHV': '8', 'W4TY': '9', '4G3F': '0', '24GB': '@', 'K9D3': '#',
               'XNQ3': '%', 'AE2O': '^', '0RSA': '&', 'NSAX': '*', 'HA3R': '(', 'PANL': ')', 'FAN3': '_', 'SNAL': '+',
               'CVK2': '-', '0F82': '=', '3BFV': '/', '34KK': '~', 'BASE': '|', 'SAN4': '\\', 'NLBU': '?', '0X3E': '.',
               '3HRJ': '$', 'IL93': '"', 'M7E2': ':', 'KV62': ';', 'LA23': ',', 'XMAP': "'", 'CP02': '>', 'V14Y': '<',
               'IDV3': '!'}
    try:
        p = ' '
        n = ''
        l = int(len(passwd) / 4)
        passwd = list(passwd)
        while 0 < l:
            l = l - 1
            n = p + n
            for x in range(0, 4):
         
                password = passwd.pop()
                n = password + n
        n = n.split(' ')
        p = n.pop(-1)
        for i in n:
            p = p + my_dict[i]
        print('\nYour Hash successful DEcrypted :D\n --> ', p)
        
    except KeyError:
        print ('key error :(\nPlease enter the password or hash completely and correctly')
        
s = input('encrypt -> 1\ndecrypt -> 2\nPlease Enter Number :  ')

if s=='1':
    encrypt()
elif s=='2':
    decrypt()
else:
    print('\nPlease enter 1 or 2')
