from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide
}

def calculator():
    print(logo)
    continue_process = True
    num1 = float(input('what\'s the first number?: ' ))
    for key in operations:
        print(key)
    while continue_process:
        symbol = input('pick an operation: ')
        num2 = float(input('what\'s the next number?: ' ))
        calculation_process = operations[symbol]
        answer = calculation_process(num1, num2)
        print(f'{num1} {symbol} {num2} = {answer}')
        q = input(f'type "y" to continue calculating with {answer} or type "n" to exit.: ')
        if q == 'y':
            num1 = answer
        else:
            continue_process = False
            calculator()
calculator()















