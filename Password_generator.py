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

        f = open("Password.txt", "a")
        f.write(Password + '\n')
        f.close()










#number = input("enter the number of passwords you wish to create: ")
#number = int(number)
    #for p in range(number):
        #import sys
        #sys.stdout = open("Password.txt", "a")
        #print(Password)
        #sys.stdout.close()

#input("Press any key to create a new Password.")


    #ans=True
    #while ans:
        #print ("""
        #1.Yes
        #0.No
        #""")
        #ans=input("What would you like to do? (write 1 for 'Yes' and 2 for 'No': ")
        
        #if ans=="1":

            #Password = 1



        #elif ans=="0":

            #Password = 0

    #if Password ==0:
        #break

#if Password==1:
    #import sys
    #sys.stdout = open("Password.txt", "a")
    #print(Password)
    #sys.stdout.close()





            #import sys
            #sys.stdout = open("Password.txt", "a")
            #print(Password)
            #sys.stdout.close()
#f = open('Password.txt', 'a')
#print('Password', file=f)
#with open('file.txt', 'a') as f:
    #print('hello world', file=f)
#f = open('helloworld.txt','w')
#f.write('hello world')
#"Password = open("Password.txt", "w")
#from random import shuffle
#print(Password_raw)
#print(Password_2)
#Password_2 = sorted(Password_1, key= lambda k: random.random())
#Password_2 = shuffle(Password_1)
#Password = ''.join(Password_2)
#from random import random
#my_list = range(10)
#shuffled_list = sorted(my_list, key=lambda x: random())

#b=array1[8]
#print(b)
