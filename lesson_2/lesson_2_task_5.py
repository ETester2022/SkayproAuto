def month_to_season(num):
        
        if (num > 2 and num < 6):
            print('Весна')
        elif (num > 5 and num < 9):
            print('Лето')
        elif (num > 8 and num < 12):
            print('Осень')
        elif (num < 1 or num > 12):
            print('Введено не верное значение!')
        else:
            print('Зима')
    
month_to_season(13)
