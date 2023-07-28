import random


print('PASSWORLD GENERATOR\n')
print(' ,o.          8 8\nd   bzzzzzzzza8o8b\n `o''\n\n')



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols  = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
mix = letters + numbers + symbols

while True:
    option = int(input('\nSelect your option\n1- 8 password characters \n2- 16 password characters\n3- Edit your password\n0-Exit\n'))

    if option == 1:
        password_8= []
        for char in range(0,8):
            password_8.append(random.choice(mix))
        print("".join(password_8))

    elif option == 2:
        password_16 = []
        for char in range(0, 17):
            password_16.append(random.choice(mix))
        print("".join(password_16))

    elif option == 3:

        password = []
        letter = int(input('How many letters: '))
        number = int(input('How many number: '))
        symbol = int(input('How many symbol: '))

        for char in range(letter):
            password.append(random.choice(letters))

        for char in range(number):
            password.append(random.choice(numbers))

        for char in range(symbol):
            password.append(random.choice(symbols))

        random.shuffle(password)
        print("".join(password))

    elif option ==0:
        break

    else:
        print('Type a valid option!')


