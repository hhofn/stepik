A = int(input())
B = int(input())
H = int(input())
if A > B:
    print ('Ошибка')
elif A <= H <= B:
    print ('Это нормально')
elif H < A:
    print ('Недосып')
elif H > B:
    print ('Пересып')