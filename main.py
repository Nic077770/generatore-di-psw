import random

elementi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza = int(input('quanti caratteri deve contenere la tua password:'))
psw = ''

for i in range(lunghezza):
    psw += random.choice(elementi)
    
print(psw)