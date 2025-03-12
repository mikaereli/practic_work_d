import random
from templates import get_username, get_answer

user_name = get_username()
print("What number is missing in the progression?")
flag = True
while flag:
    length = random.randint(5, 10)
    numbers = [0] * length
    q = random.randint(2, 7)
    print("Question:", end=" ")
    for i in range(length):
        if i == 0:
            numbers[i] = random.randint(1, 7)
            continue
        numbers[i] = numbers[i-1] * q

    hiden = random.randint(1, length-2)

    for i in range(length):
        if i == hiden:
            print("..", end=" ")
            continue
        print(numbers[i], end=" ")

    print()
    print("Your answer:")
    user_answer = int(input())
    flag = get_answer(numbers[hiden], user_answer)
