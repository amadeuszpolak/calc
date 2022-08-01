import logging

def convert_if_not_number(var):
    while var is not int or var is not float:
        try:
            var = float(var)
            break
        except ValueError:
            print('Podaj składnik jeszcze raz, składnik musi być liczbą. ')
            var = input("Podaj składnik. ")
    return var

logging.basicConfig(level=logging.DEBUG)
result = 0

#Operation input
operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
while operation != '1' and operation != '2' and operation != '3' and operation != '4':
    print("Podaj liczbę z zakresu 1-4")
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

#Components of operation input
comp1 = input("Podaj składnik 1. ")
comp1 = convert_if_not_number(comp1)
comp2 = input("Podaj składnik 2. ")
comp2 = convert_if_not_number(comp2)
add_list = []
multiply_list = []

#Add operation
if operation == '1':
    add_list.append(comp1)
    add_list.append(comp2)
    comp_input = input("Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    while comp_input != 'n' and comp_input != 'N':
        if comp_input != 'n' and comp_input != 'N':
            comp_input = convert_if_not_number(comp_input)
            add_list.append(comp_input)
        comp_input = input("Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    logging.info("Dodaję %s" % add_list)
    for i in add_list:
        result += i

#Sub Operation
elif operation == '2':
    logging.info("Odejmuję %s i %s" % (comp1, comp2))
    result = comp1-comp2

#Multiply Operation
elif operation == '3':
    multiply_list.append(comp1)
    multiply_list.append(comp2)
    comp_input = input("Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    while comp_input != 'n' and comp_input != 'N':
        if comp_input != 'n' and comp_input != 'N':
            comp_input = convert_if_not_number(comp_input)
            multiply_list.append(comp_input)
        comp_input = input("Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    logging.info("Dodaję %s" % multiply_list)
    result = 1
    for i in multiply_list:
        result *= i

#Div Operation
elif operation == '4':
    logging.info("Dzielę %s i %s" % (comp1, comp2))
    while comp2 == 0:
        print("Nie można dzielić przez 0")
        comp2 = input("Podaj składnik 2. ")
        comp2=convert_if_not_number(comp2)
    result = comp1/comp2

#Show result
print("Wynik to %f" % result)