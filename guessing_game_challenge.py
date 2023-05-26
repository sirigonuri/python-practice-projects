import random

number = random.randint(1,100)
print(number)
while True:
    guess_number = 0
    new_number = int(input("Please guess a number between 1 and 100:"))
    if abs(number-new_number)<=10:
        print("Warm")
        new_number_1 = int(input("close! guess the new number :"))

    else:
        print("cold")


    # if new_number < 1 or new_number > 100:
    #     print("The number you have entered is OUT OF BOUNDS")
    #     guess_number=guess_number+1
    #     continue
    # elif new_number > 1 or new_number < 100:
    #     a = number + 10
    #     b = number - 10
    #     if new_number == number:
    #         print("You won!!, You have guessed the correct number")
    #         print(guess_number)
    #         break
    #     elif (new_number >= b) and (new_number <= a):
    #         print("Warm!, you are close. Try another number")
    #         guess_number=guess_number+1
    #         continue
    #     else:
    #         print("Cold, you are very far from the correct number. Try another number")
    #         guess_number=guess_number+1
    #         continue