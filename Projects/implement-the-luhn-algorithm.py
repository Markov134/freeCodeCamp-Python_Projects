def verify_card_number(card_number):
    card_translation = card_number.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    reversed_card_number = translated_card_number[::-1]
    
    sum = 0
    for i in range(len(reversed_card_number)):
        result = int(reversed_card_number[i])
        if i % 2 == 1:
            result *= 2

        if result > 9:
            result -= 9
            sum += result
            print(result, 'after')
        else:
            sum += result
            print(result, 'result')

    print(sum, 'sum')
    print(sum % 10, 'mod')

    if sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'


hi = '453914881'
result = verify_card_number(hi)
print(result, '\n')


new = '4111-1111-1111-1111'
result = verify_card_number(new)
print(result)

