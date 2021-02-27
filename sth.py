
def konwerter (system_zapisu, liczba, nowy_system):
  '''Polish alert, sorry
     funkcja przyjmuje liczbe do konwersji oraz system w ktorym ta liczba jest zapisana i 
     system w ktorym liczba ma byc zapisna
     zwraca slownik {system_liczby_podanej : podana_liczba, system_na_ktory_ma_byc_zmieniona : zmieniona_liczba}'''
    result = {system_zapisu : liczba, nowy_system : 0}
    if type(liczba) != str:
        str(liczba)
        
    for index, wartosc in enumerate(liczba):
        #len(liczba) - index - 1 = potega
        temp = 0
        if wartosc <= '9' and wartosc >= '0': # dla liczb 0 - 9
            temp = ord(wartosc) - ord(0) # ord('1') - ord('0') = 1
        else: # dla liter
            temp = ord(wartosc)-87 # ord('a')-87 = 10
        temp = temp * system_zapisu**(len(liczba) - index - 1)
        result[nowy_system] = result[nowy_system] + temp
    
    if nowy_system != 10:
        temp = []
        while result[nowy_system] != 0:
            temp.append(result[nowy_system]%nowy_system)
            result[nowy_system] = int(result[nowy_system]/nowy_system)
        temp.reverse()
        
        for i, el in enumerate(temp):
            if el < 10:
                temp[i] = str(el)
            else:
                temp[i] = chr(el+87) # chr(10+87) = 'a'
                
        result[nowy_system] = ''.join(temp)
        
    return result


def main():
    print("This programm let's you change any number written in any numerical system to this number in any other numerical system")
    print('Pls only int input')
    number = 0
    sys1 = 10
    sys2 = 10
    try:
        number = int(input('give me a number: '))
        sys1 = int(input('write numeric base of your number: '))
        sys2 = int(input('write numeric base u want to conver your number: '))
    Except:
        print('ugh, told u')
    
    number_converted = konwerter(sys1, number, sys2)
    
    print('--------------------------------')
    print('converted number = ', end = '')
    print(number_converted)

if __name__ == "__main__":
    main()
