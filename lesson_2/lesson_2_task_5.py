def month_to_season(num):

    for num in range(1, 13):

        if (num > 2 and num < 6):
            print('Весна')
        elif (num > 5 and num < 9):
            print('Лето')
        elif (num > 8 and num < 12):
            print('Осень')
        else:
            print('Зима')
    
month_to_season(3)

# Цикл использовал для того чтоб ограничить ввод количеством месяцев в году

# Идей для решения нет