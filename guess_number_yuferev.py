import numpy as np

a = 1 # input ('Диапазон от: ')
b = 100 # input ('Диапазон до: ')

#number = np.random.randint(a, b+1)    # загадали число
# print (f"Загадано число от {a} до {b}: {number}")

count_ls = [] # список количества попыток

def game_core_v4(number):
    # вводим изменяемые переменные сужаемого диапазона
    a_1 = a 
    b_1 = b
    for count in range(a, b+1):
        predict = np.random.randint(a_1, b_1+1) # выбираем рандомное число из суженного диапазона
        if predict == number: break    # выход из цикла, если угадали
        elif number > (a_1 + b_1)//2: # если загаданное число больше половины урезанного диапазона
            a_1 = ((a_1 + b_1)//2)+1 # то увеличить нижнюю планку диапазона на 1
        elif number < (a_1 + b_1)//2: # если загаданное число меньше половины урезанного диапазона
            b_1 = ((a_1 + b_1)//2)-1 # то уменьшить верхнюю планку диапазона на 1
    
    return(count) # возврат из функции числа попыток
    #return(count)(f"Вы угадали число {number} за {count} попыток.")
    
def score_game(game_core_v4):
    random_array = np.random.randint(a, b+1, size=(1000)) # задаем диапазон и количество попыток
    for number in random_array:
        count_ls.append(game_core_v4(number))
    score = int(np.mean(count_ls)) # из полученных количества попыток вычисляем среднее и переводим формат в число
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
#game_core_v4(number)
score_game(game_core_v4)