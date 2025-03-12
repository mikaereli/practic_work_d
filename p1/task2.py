import random

from templates import get_username, get_answer
from generator import generate_numbers

user_name = get_username()
print("What number is missing in the progression?")
flag = True
while flag:
    length = random.randint(5, 10)
    numbers = generate_numbers(length=length, is_task_1=False)

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
