koloda = [6,7,8,9,10,2,3,4,11] * 4


from random import shuffle
shuffle(koloda)

count = 0

while True:
    choice = input('будете брать карту? yes/no\n')
    if choice == 'yes':
        current = koloda.pop()
        print(f'вам попалась карта достоинством {current}')
        count+= current
        if count > 21:
            print('вы проиграли')
            break
        elif count == 0:
            print('вы выиграли')
            break
        else:
            print(f'у вас {count} очков')
    if choice == 'no':
        print('у вас %d очков и вы закончили игру' %count)
        break

print('goodbuy')

