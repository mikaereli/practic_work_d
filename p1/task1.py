from math import lcm
import random
from templates import get_username, get_answer


user_name = get_username()
print("Find the smallest common multiple of given numbers.")
flag = True
while flag:
    numbers = []

    for _ in range(3):
        numbers.append(random.randint(1, 100))

    print("Question: ", numbers[0], numbers[1], numbers[2], "\nYour answer:")
    answer = lcm(numbers[0], numbers[1], numbers[2])
    user_answer = int(input())
    flag = get_answer(answer, user_answer)
