import sys

def getCoef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    try:
        coef = float(coef_str)
    except:
        while True:
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
            except:
                continue
            break
    return coef

def getDisc(a, b, c):
    return int(b) * int(b) - 4 * int(a) * int(c)

def getSolution(a, b, c):
    temp = getDisc(a, b, c)
    if temp < 0:
        print("Решений нет")
    if temp >= 0:
        D = temp ** (0.5)
        y1 = (((int(b)) * (-1) + D) / 2 * int(a))
        y2 = (((int(b)) * (-1) - D) / 2 * int(a))
        print("y1 = " + str(y1))
        print("y2 = " + str(y2))
        print()
        if (y1 < 0 and y2 < 0):
            print("Решений нет")
        if (y1 == y2 and y1 >= 0):
            x1 = y1 ** (0.5)
            print("x1 = x2 = x3 = x4 =" + str(x1))
        if (y1 != y2):
            if (y1 > 0):
                x1 = y1 ** (0.5)
                print("x1 = " + str(x1) + " x2 = " + str(x1 * (-1)))
            else:
                print("Нет действительных корней x1, x2")
            if (y2 > 0):
                x2 = y2 ** (0.5)
                print("x3 = " + str(x2) + " x4 = " + str(x2 * (-1)))
            else:
                print("Нет действительных корней x3, x4")
    print("\nСысоев А. Н. РТ5-51Б\n")

def main():
    a = getCoef(1, 'Введите коэффициент a:')
    b = getCoef(2, 'Введите коэффициент b:')
    c = getCoef(3, 'Введите коэффициент c:')
    print()
    getSolution(a, b, c)

if __name__ == "__main__":
    main()
