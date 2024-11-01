import random

main_menu = 'Main menu \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit'


def add_numbers():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    sum = num1 + num2
    answer = int(input(f'What is {num1} + {num2}? '))
    if answer == sum:
        print('Way to go!!')
    else:
        print(f'Sorry, the correct answer is {sum}. Try another one.')


def subtract_numbers():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    if num1 < num2:
        num1 = num2
    difference = num1 - num2
    answer = int(input(f'What is {num1} - {num2}? '))
    if answer == difference:
        print('You got it right!!')
    else:
        print(f'Sorry, the correct answer is {difference}. Try another one.')


def multiply_numbers():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2
    answer = int(input(f'What is {num1} * {num2}? '))
    if answer == product:
        print('Super work!!!')
    else:
        print(f'Sorry, the correct answer is {product}. Try another one.')


def divide_numbers():
    num1 = random.randint(0, 9)
    num2 = random.randint(1, 9)
    dividend = num1 / num2
    answer = int(input(f'What is {num1} / {num2}? '))
    if answer == dividend:
        print('Look at you go!!')
    else:
        print(f'Sorry, the correct answer is {dividend}. Try another one.')


print(main_menu)
choice = int(input("Enter a choice: "))

while choice != 5:
    if choice == 1:
        add_numbers()
        print(main_menu)
        choice = int(input("Enter a choice: "))
    elif choice == 2:
        subtract_numbers()
        print(main_menu)
        choice = int(input("Enter a choice: "))
    elif choice == 3:
        multiply_numbers()
        print(main_menu)
        choice = int(input("Enter a choice: "))
    elif choice == 4:
        divide_numbers()
        print(main_menu)
        choice = int(input("Enter a choice: "))
    else:
        print("Choice not valid")
        choice = int(input("Enter a choice: "))
print("Thank you for playing")