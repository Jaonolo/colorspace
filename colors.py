from math import floor

def main():
    colors = registerColors()
    coeff = leastSquaresColors(colors)
    print('==================')
    while True:
        c = input('um codigo hex ou x para parar: ')
        if(c == 'x'):
            break
        elif(checkIfColorCode(c)):
            n = 2
            color = [int((c[1::])[i : i + n], base=16) for i in range(0, len(c[1::]), n)]
            newColor = [f'{floor(coeff[i][0] + color[i]*coeff[i][1])}' for i in range(len(color))]
            newColor = '(' + ','.join(newColor) + ')'
            print(f'{c} turns into {newColor}')
        else:
            print('não é x nem um codigo hex!')


def leastSquaresColors(colors):
    r = [(colors[i][0][0], colors[i][1][0]) for i in range(len(colors))]
    g = [(colors[i][0][1], colors[i][1][1]) for i in range(len(colors))]
    b = [(colors[i][0][2], colors[i][1][2]) for i in range(len(colors))]
    return (leastSquares(r), leastSquares(g), leastSquares(b))



def leastSquares(data):
    x_mean, y_mean, a, b = [0]*4
    for x, y in data:
        print(f'{x} turns into {y}')
        x_mean += x
        y_mean += y
        a += x*y
        b += x**2
    n = len(data)
    b = (n*a - x_mean - y_mean)/(n*b + (x_mean)**2)
    a = (y_mean/n) - b*(x_mean/n)
    return (a, b)

def registerColors():
    colors = []
    while True:
            a = input('um codigo hex ou x para parar: ')
            if(a == 'x'):
                break
            elif(checkIfColorCode(a)):
                n = 2
                while True:
                    b = input('mais um codigo hex ou x para ignorar: ')
                    if(b == 'x'):
                        colors += [(
                            [int((a[1::])[i : i + n], base=16) for i in range(0, len(a[1::]), n)],
                            False
                        )]
                        break
                    elif(checkIfColorCode(b)):
                        colors += [(
                            [int((a[1::])[i : i + n], base=16) for i in range(0, len(a[1::]), n)],
                            [int((b[1::])[i : i + n], base=16) for i in range(0, len(b[1::]), n)]
                        )]
                        break
                    else:
                        print('não é x nem um codigo hex!')
            else:
                print('não é x nem um codigo hex!')
    print(colors)
    return colors

# Primeira versão, trocar para regex e ver se HEX só tem 0 ~ F
def checkIfColorCode(colorCode):
    if(not colorCode.startswith('#') or len(colorCode) != 7):
        return False
    return True

if(__name__ == '__main__'):
    main()