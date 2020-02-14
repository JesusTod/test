from enum import Enum
days = range (1, 32)
mounths = range (1, 13)
years = range (1901, 2020)
d, m, y = int (input ( 'day:')), \
int (input ( 'mounth:')), \
int (input ( 'year:'))
if d in days and m in mounths and y in years:
    if m == 4 or m == 6 or m == 9 or m == 11:         # прошлые месяцы по 31 д
        if d == 1:
            print(31,m-1,y)
            print(d+1,m,y)
        elif d == 31:
            print(d-1,m,y)
            print(1,m+1,y)
        else:
            print(d-1,m,y)
            print(d+1,m,y)

    elif m == 1 or m == 8:                           # прошлые месяцы по 31, и они сами 31
        if m == 1 and d == 1:
            print(31,12,y-1)
            print(d+1,m,y)
        elif d == 31:
            print(d-1,m,y)
            print(1,m+1,y)
        else:
            print(d-1,m,y)
            print(d+1,m,y)
    elif m == 5 or m == 7 or m ==10:                 # прошлые месяцы по 30 дней
        if d == 1:
            print(30,m-1,y)
            print(d+1,m,y)
        elif d == 31:
            print(d-1,m,y)
            print(1,m+1,y)
        else:
            print(d-1,m,y)
            print(d+1,m,y)

    elif m == 12:                                  #вероятность НГ
        if d == 1:
            print(30,m-1,y)
            print(d+1,m,y)
        elif d == 31:
            print(d-1,m,y)
            print(1,1,y+1)
        else:
            print(d-1,m,y)
            print(d+1,m,y)

    if m == 2 and y % 4 == 1:               # высокосный год февраля
        if d == 1:
            print(31,m-1,y)
            print(d+1,m,y)
        elif d == 28:
            print(1,m+1,y)
            print(d-1,m,y)
        else:
            print(d-1,m,y)
            print(d+1,m,y)

    if m == 2 and y % 4 != 1:
        if d == 29:
            print(1, m + 1, y)
            print(d - 1, m, y)
        elif d == 1:
            print(31, m - 1, y)
            print(d + 1, m, y)
        else:
            print(d - 1, m, y)
            print(d + 1, m, y)

    elif m == 3:
        if d == 1:
            if y % 4 == 0:                  # если высокосный год марта 1 числа
                print(29,m-1,y)
                print(d+1,m,y)
            else:
                print(28,m-1,y)
                print(d+1,m,y)
        elif d == 31:
            print(1,m+1,y)
            print(d-1,m,y)
        else:
            print(d-1,m,y)
            print(d+1,m,y)





i = float(input('Введіть від 0 до 60'))
if 0 <= i <= 60:
    while i > 6:
        i -= 6
    if 0 <= i < 3 or i == 6:
        print('Green')
    elif 3 <= i < 4:
        print('Yellow')
    elif 4 <= i < 6:
        print('Red')



class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
s = month [input ( 'month:')]
if s == month.March or s == month.April or s ==  month.May:
    print(season.Spring)
elif s == month.June or s == month.July or s == month.August:
    print(season.Summer)
elif s == month.September or s== month.October or s == month.November:
    print(season.Autumn)
else:
    print(season.Winter)




class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4
x = float (input ( 'amount of money:'))
p = converter [input ( 'currency:')]
usd = float(24.43)
eur = float(26.67)
czk = float(1.07)
pln = float(6.26)
if p == converter.USD:
    print(usd*x)
elif p == converter.EUR:
    print(eur*x)
elif p == converter.CZK:
    print(czk*x)
else:
    print(pln*x)