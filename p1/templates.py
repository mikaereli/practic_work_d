
def get_username():
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = str(input())
    print(f"Hello, {user_name}!")
    return user_name


def get_answer(current_answer, user_answer):
    if user_answer == current_answer:
        print("Correct!")
        return True
    else:
        print(user_answer, "is wrong answer ;(. Correct answer was", current_answer, ".")
        return False
