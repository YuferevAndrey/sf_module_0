import numpy as np

a = 1 #input ('Диапазон от: ')
b = 100 #input ('Диапазон до: ')

number = np.random.randint(a, b+1)    # загадали число
#print (f"Загадано число от 1 до 99: {number}")

a_1 = a
b_1 = b

for count in range(a, b+1):
    predict = np.random.randint(a_1, b_1+1)
    if number == (a_1 + b_1)//2: break    # выход из цикла, если угадали
    elif number > (a_1 + b_1)//2:
        a_1 = ((a_1 + b_1)//2)+1
#        print (f"Угадываемое число больше {predict} ")
    elif number < (a_1 + b_1)//2:
        b_1 = ((a_1 + b_1)//2)-1
#        print (f"Угадываемое число меньше {predict} ")
        
print (f"Вы угадали число {number} за {count} попыток.")