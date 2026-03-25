def number_pattern(n):
    if type(n) is not int:
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    number_string = ''
    for number in range(1, n + 1):
        number_string += str(number)
        if number != n:
            number_string += ' '
    return number_string

number_pattern(4)
