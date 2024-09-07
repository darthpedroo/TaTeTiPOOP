def is_input_a_valid_int(input):
    try:
        int(input)
    except ValueError:
        print("INGRESA UN NÚMERO, NO UN TEXTO")
        return False
    if int(input) < 0:
        print("INGRESA UN NÚMERO MAYOR A 0")
        return False
    return True


def is_input_greater_than_zero(input):
    try:
        int(input)
    except ValueError:
        print("INGRESA UN NÚMERO, NO UN TEXTO")
        return False
    if int(input) <= 0:
        print("INGRESA UN NÚMERO MAYOR A 0")
        return False
    return True
