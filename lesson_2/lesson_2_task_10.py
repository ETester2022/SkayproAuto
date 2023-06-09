#x = 'vklad'
#y = 'srok'
#bonus = 0.1

#def bank(x, y):

#    for y in range(1, (y + 1), 1):
#        b = x * bonus + x 
#        c = b * bonus + x
#        print(c)

#bank(100, 3)

s = int(input())
p = int(input())
k = int(input())

total = s * (1 + p/100) ** k
print(total)