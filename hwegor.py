import random
def game():
    attempts = 0
    level = input("Какой уровень сложности вы хотите выбрать? \n Введите: \n '1', если Новичок \n '2', если Любитель \n '3', если Профессионал \n")
    level = int(level)
    limit = input("Выберите предел рандома: ")
    limit = int(limit)
    random_number = random.randint(1, limit)
    print("Пора проверить свою удачу! ")
    if level in [1]:    #прописываем кол-во попыток в зависимости от уровня
        num_attempts = 12
    if level in [2]:
        num_attempts = 9
    if level in [3]:
        num_attempts = 6

    while attempts < num_attempts:  #крутим количество попыток согласно выбранному уровню игры
        guess_number = input("Угадайте число: ")
        guess_number = int(guess_number)
        attempts = attempts + 1

        if random_number < guess_number:
            print("Нужно поменьше")
        if random_number > guess_number:
            print("Нужно побольше")

        if (random_number <= guess_number + 6) and (random_number >= guess_number - 6):
            print("Горячо")
        if (random_number > guess_number + 6) or (random_number < guess_number - 6):
            print("Холодно")
        if random_number == guess_number:
            break

    if guess_number == random_number:
        attempts = str(attempts)
        print("Превосходно! Ты угадал число с " + attempts + " попытки. ")
    if guess_number != random_number:
        random_number = str(random_number)
        print("К сожалению, вы не угадали число " + random_number + ", но не расстраивайтесь, вам еще обязательно повезет!") #утешил
    game()
game()