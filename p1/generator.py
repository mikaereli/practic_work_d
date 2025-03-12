import random


def generate_numbers(length=3, is_task_1=True):
    numbers = [0] * length
    if is_task_1:
        for i in range(length):
            numbers[i] = random.randint(1, 100)
    else:
        q = random.randint(2, 7)
        print("Question:", end=" ")
        for i in range(length):
            if i == 0:
                numbers[i] = random.randint(1, 7)
                continue
            numbers[i] = numbers[i-1] * q
    return numbers
