from furniture import (Table, Closet, Other_furniture)

def main():
    furnitures = count_of()





def count_of():
    s = []
    cont = True
    while (cont):
        print('Выберите какой вид мебели вы хотите добавить:\n')
        print('1 - Table\n2 - Closet\n3 - Other')
        correct = False
        while (correct==False):
            try:
                n=-1
                while (n<0 or n>3):
                 n = int(input())
            except ValueError:
                print('Ошибка!')
                correct = False
            try:
                count=0
                while (count<=0):
                    count = int(input('Введите количество мебели(положительное число): '))
                correct = True
            except ValueError:
                print('Ошибка!')
                correct = False
        if n==1:
            for i in range(count):
                t = Table(int(input('Length: ')), int(input('Width: ')))
                s.append(t)
        if n==2:
            for i in range(count):
                t = Closet(int(input('Length: ')), int(input('Width: ')))
                s.append(t)
        if n==3:
            for i in range(count):
                t = Other_furniture(int(input('Length: ')), int(input('Width: ')))
                s.append(t)
        print('Хотите добавить еще мебели? YES/NO')
        answer = input().upper()
        if (answer=='NO'): cont = False
    return s





if __name__ =='__main__':
    main()
