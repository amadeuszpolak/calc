import logging


def convert_if_not_number(var):
    while True:
        try:
            var = float(var)
            break
        except ValueError:
            print('Podaj składnik jeszcze raz, składnik musi być liczbą. ')
            var = input("Podaj składnik. ")
    return var


def add(var1, var2):
    sum = var1+var2
    logging.info("Dodaję %s i %s" % (var1, var2))
    comp_input = input(
        "Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    while comp_input.lower() != 'n':
        comp_input = convert_if_not_number(comp_input)
        sum += comp_input
        logging.info("Suma została powiększona o %s" % comp_input)
        comp_input = input(
            "Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    return sum


def sub(var1, var2):
    logging.info("Odejmuję %s i %s" % (var1, var2))
    return var1-var2


def multiply(var1, var2):
    result = var1*var2
    logging.info("Mnożę %s i %s" % (var1, var2))
    comp_input = input(
        "Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    while comp_input.lower() != 'n':
        comp_input = convert_if_not_number(comp_input)
        result *= comp_input
        logging.info("Iloczyn został pomnożony przez %s" % comp_input)
        comp_input = input(
            "Podaj kolejny składnik lub 'N' jeśli chcesz zakończyć podawanie składników. ")
    return result


def div(var1, var2):
    while var2 == 0:
        print("Nie można dzielić przez 0")
        var2 = input("Podaj składnik 2. ")
        var2 = convert_if_not_number(var2)
        logging.info("Dzielę %s i %s" % (var1, var2))
    return var1/var2


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    while True:
        next_operation = ''
        result = 0
        # Operation input
        operation = input(
            "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        while operation not in {"1", "2", "3", "4"}:
            print("Podaj liczbę z zakresu 1-4")
            operation = input(
                "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        # Components of input operation
        comp1 = input("Podaj składnik 1. ")
        comp1 = convert_if_not_number(comp1)
        comp2 = input("Podaj składnik 2. ")
        comp2 = convert_if_not_number(comp2)
        # Add operation
        if operation == '1':
            result = add(comp1, comp2)
        # Sub Operation
        elif operation == '2':
            result = sub(comp1, comp2)
        # Multiply Operation
        elif operation == '3':
            result = multiply(comp1, comp2)
        # Div Operation
        elif operation == '4':
            result = div(comp1, comp2)
        # Show result
        print("Wynik to %f" % result)
        next_operation = input("Czy chcesz zakończyć (T)?")
        if next_operation.lower() == 't':
            break
