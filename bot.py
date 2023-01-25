print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
user_int = int(input())
count_value = 0
while count_value <= user_int:
    print(count_value, " !")
    count_value += 1;
print('Completed, have a nice day!')
print("Let's test your programming knowledge.")
print('Why do we use methods?')
answers = ['1. To repeat a statement multiple times.',
           '2. To decompose a program into several small subroutines.',
           '3. To determine the execution time of a program.',
           '4. To interrupt the execution of a program.',]
for item in answers:
    print(item)
user_answer = input()
while user_answer != '2':
    print('Please, try again!')
    user_answer = input()
else:
    print('Congratulations, have a nice day!')