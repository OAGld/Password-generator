import random

array1 = '1234567890'
array2 = '!"#¤%&/(=?,.-;:_'
array3 = 'qwertyuiopasdfghjklzxcvbnm'
array4 = 'QWERTYUIOPASDFGHJKLZXCVBNM'


while 1==1:   
        Password = ''
        for c in range(2):
            Password += random.choice(array1)
        for c in range(2):
            Password += random.choice(array2)
        for c in range(4):
            Password += random.choice(array3)
        for c in range(2):
            Password += random.choice(array4)

        Password = list(Password)

        Password = random.sample(Password, 10)

        Password = ''.join(Password)

        name = input("What's the password for?:")

        Password = name+': ', Password

        Password = ''.join(Password)

        Password = str(Password)

        print(Password)

        #Input which file you would like to write to in "file".
        f = open("file", "a")
        f.write(Password + '\n')
        f.close()
