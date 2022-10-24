def main():
    colors = []
    while True:
        a = input('um codigo hex ou x para parar: ')
        if(a == 'x'):
            break
        elif(checkIfColorCode(a)):
            colors += [a]
        else:
            print('não é x nem um codigo hex!')
    print(colors)
    

# Primeira versão, trocar para regex e ver se HEX só tem 0 ~ F
def checkIfColorCode(colorCode):
    if(not colorCode.startswith('#') or len(colorCode) != 7):
        return False
    return True

if __name__ == '__main__':
    main()